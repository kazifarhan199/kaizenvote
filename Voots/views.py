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
from .models import Voots_model
from django.shortcuts import get_object_or_404


class Voots_list_view(ListView):
    model = Title_model
    paginate_by = 7
    template_name = 'Voots/list_view.html'

    def get_queryset(self):
        context  = self.model.objects.filter(publish=True)
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

class Voots_create_view(CreateView):
    model = Voots_model
    fields = []
    template_name = 'Title/create_view.html'

    def form_valid(self, form):
        form.instance.ip = get_client_ip(self.request)
        option = self.request.POST.get('option')
        option = get_object_or_404(Options_model, pk=option)
        
        if not(option.title.publish):
            raise Exception("Can't vote for unpublished title")

        option.votes += 1
        option.save()
        return super(Voots_create_view, self).form_valid(form)

    def get_success_url(self):
        url = self.request.META['HTTP_REFERER'].rsplit('/',1)[1]
        return reverse_lazy('Voots-detail', args=[url,])



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip