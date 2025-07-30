from django.urls import path
from . import views

urlpatterns = [
    path("", views.AITListView.as_view(), name="AIT_list"),
    path("create/", views.AITCreateView.as_view(), name="AIT_create"),
    path("<int:pk>/update/", views.AITUpdateView.as_view(), name="AIT_update"),
    path("<int:pk>/delete/", views.AITDeleteView.as_view(), name="AIT_delete"),
]