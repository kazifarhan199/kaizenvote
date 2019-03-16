from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Options_model
from django.db.models import Q

class Options_list_view(ListView):
    model = Options_model
    template_name = 'Options/list_view.html'

class Options_detail_view(DetailView):
    model = Options_model
    template_name = 'Options/detail_view.html'

class Options_create_view(CreateView):
    model = Options_model
    fields = ['title','name', 'd1', 'd2', 'd3', 'image']   
    template_name = 'Options/create_view.html'

    def get_success_url(self):
        url = self.request.META['HTTP_REFERER'].rsplit('/',1)[1]
        return reverse_lazy('Title-detail', args=[url,])

class Options_delete_view(DeleteView):
    model = Options_model
    template_name = 'Options/delete_view.html'
    success_url = reverse_lazy('Options-list')		

class Options_edit_view(UpdateView):
    model = Options_model
    template_name = 'Options/create_view.html'
    fields = ['title','name', 'd1', 'd2', 'd3', 'image']   

    def get_success_url(self):
        url = self.request.META['HTTP_REFERER'].rsplit('/',1)[1]
        return reverse_lazy('Title-detail', args=[url,])

