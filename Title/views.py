from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Title_model
from django.db.models import Q
from Options import models

class Title_list_view(ListView):
    model = Title_model
    paginate_by = 7
    template_name = 'Title/list_view.html'

    def get_queryset(self):
        context  = self.model.objects.filter(user=self.request.user)
        q = self.request.GET.get('q')
        if q:
            query = Q()
            for i in q.split():
                query.add(Q(title__icontains=i), Q.OR)
            context  = context.filter(query).order_by('-id')
        else:
            context = context.all().order_by('-id')
        return context

class Title_detail_view(DetailView):
    model = Title_model
    template_name = 'Title/detail_view.html'

    def get_context_data(self, **kwargs):
        context = super(Title_detail_view, self).get_context_data(**kwargs)
        context['options'] = models.Options_model.objects.filter(title=context['object'])
        return context

class Title_create_view(CreateView):
    model = Title_model
    fields = ['title', 'discription']   
    template_name = 'Title/create_view.html'
    success_url  = reverse_lazy('Title-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Title_create_view, self).form_valid(form)

class Title_delete_view(DeleteView):
    model = Title_model
    template_name = 'Title/delete_view.html'
    success_url = reverse_lazy('Title-list')		

class Title_edit_view(UpdateView):
    model = Title_model
    template_name = 'Title/create_view.html'
    fields = ['title', 'discription']   

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.publish:
            form.errors["error"]="Can't edit Published Title"
            return super(Title_edit_view, self).form_invalid(form, *args, **kwargs)

        return super(Title_edit_view, self).form_valid(form)

    def get_success_url(self):
        url = self.request.META['HTTP_REFERER'].rsplit('/',1)[1]
        return reverse_lazy('Title-detail', args=[url,])

class Title_publish_view(UpdateView):
    model = Title_model
    template_name = 'Title/create_view.html'
    fields = ['publish','end_date']

    def get_success_url(self):
        url = self.request.META['HTTP_REFERER'].rsplit('/',1)[1]
        return reverse_lazy('Title-detail', args=[url,])
