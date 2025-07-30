from django.shortcuts import render
from .models import Benchmark
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 


class BenchmarkListView(ListView):
    model = Benchmark
    template_name = 'benchmark/benchmark_list.html'
    context_object_name = 'benchmarks'

class BenchmarkCreateView(CreateView):
    model = Benchmark
    template_name = 'benchmark/benchmark_form.html'
    fields = ['__all__']
    success_url = '/benchmark/'

class BenchmarkUpdateView(UpdateView):
    model = Benchmark
    template_name = 'benchmark/benchmark_form.html'
    fields = ['__all__']
    success_url = '/benchmark/'


class BenchmarkDeleteView(DeleteView):
    model = Benchmark
    template_name = 'benchmark/benchmark_confirm_delete.html'
    success_url = '/benchmark/'