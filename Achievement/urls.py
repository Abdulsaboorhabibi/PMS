from django.urls import path
from . import views

urlpatterns = [
    path("", views.AchievementListView.as_view(), name="Achievement_list"),
    path("create/", views.AchievementCreateView.as_view(), name="Achievement_create"),
    path("<int:pk>/update/", views.AchievementUpdateView.as_view(), name="Achievement_update"),
    path("<int:pk>/delete/", views.AchievementDeleteView.as_view(), name="Achievement_delete"),
]