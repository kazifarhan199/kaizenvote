from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from Title.models import Title_model
from django.db.models import Q
from Options.models import Options_model 

# Create your views here.

class Voots_list_view(ListView):
    model = Title_model
    paginate_by = 7
    template_name = 'Voots/list_view.html'

    def get_queryset(self):
        context  = self.model.objects.all()
        q = self.request.GET.get('q')
        if q:
            query = Q()
            for i in q.split():
                query.add(Q(title__icontains=i), Q.OR)
            context  = context.filter(query).order_by('-id')
        else:
            context = context.all().order_by('-id')
        return context

class Voots_detail_view(DetailView):
    model = Title_model
    template_name = 'Voots/detail_view.html'

    def get_context_data(self, **kwargs):
        context = super(Voots_detail_view, self).get_context_data(**kwargs)
        context['options'] = Options_model.objects.filter(title=context['object'])
        return context
