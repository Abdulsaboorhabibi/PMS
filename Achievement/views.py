from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Achievement

class AchievementListView(ListView):
    model = Achievement
    template_name = 'achievement/achievement_list.html'
    context_object_name = 'achievements'

class AchievementCreateView(CreateView):
    model = Achievement
    template_name = 'achievement/achievement_form.html'
    fields = ['__all__']
    success_url = '/achievement/'

class AchievementUpdateView(UpdateView):
    model = Achievement
    template_name = 'achievement/achievement_form.html'
    fields = ['__all__']
    success_url = '/achievement/'

class AchievementDeleteView(DeleteView):
    model = Achievement
    template_name = 'achievement/achievement_confirm_delete.html'
    success_url = '/achievement/'

    