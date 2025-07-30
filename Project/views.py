from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Project
from django.contrib import messages
from .forms import ProjectForm

class ProjectListView(ListView):
    model = Project
    template_name = 'Project/index.html'
    context_object_name = 'projects'


class ProjectCreateView(CreateView):
    model = Project
    #fields = ['title', 'start_date', 'end_date', 'province', 'district', 'description']
    form_class = ProjectForm
    template_name = 'Project/project_form.html'
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, 'Project created successfully!')
        return super().form_valid(form)


class ProjectUpdateView(UpdateView):
    model = Project
    #fields = ['title', 'start_date', 'end_date', 'province', 'district', 'description']
    form_class = ProjectForm
    template_name = 'Project/project_form.html'
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, 'Project updated successfully!')
        return super().form_valid(form)

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'Project/project_confirm_delete.html'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Project deleted successfully!')
        return super().delete(request, *args, **kwargs)