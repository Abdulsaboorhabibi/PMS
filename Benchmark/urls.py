from django.urls import path
from . import views

urlpatterns = [
    path("", views.BenchmarkListView.as_view(), name="benchmark_list"),
    path("create/", views.BenchmarkCreateView.as_view(), name="benchmark_create"),
    path("<int:pk>/update/", views.BenchmarkUpdateView.as_view(), name="benchmark_update"),
    path("<int:pk>/delete/", views.BenchmarkDeleteView.as_view(), name="benchmark_delete"),
]