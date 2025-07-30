from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from .models import AIT

class AITListView(ListView):
    model = AIT
    template_name = 'AIT/AIT_list.html'
    context_object_name = 'AITs'


class AITCreateView(CreateView):
    model = AIT
    template_name = 'AIT/AIT_form.html'
    fields = ['__all__']
    success_url = '/AIT/'

class AITUpdateView(UpdateView):
    model = AIT
    template_name = 'AIT/AIT_form.html'
    fields = ['__all__']
    success_url = '/AIT/'

class AITDeleteView(DeleteView):
    model = AIT
    template_name = 'AIT/AIT_confirm_delete.html'
    success_url = '/AIT/'