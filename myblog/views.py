from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from myblog.models import Myblog


class MyblogCreateView(CreateView):
    model = Myblog
    fields = ('title', 'slug', 'body', 'preview', 'created_at', 'public', 'views_counter')
    success_url = reverse_lazy('myblog:list')


class MyblogListView(ListView):
    model = Myblog


class MyblogUpdateView(UpdateView):
    model = Myblog
    fields = ('title', 'slug', 'body', 'preview', 'created_at', 'public', 'views_counter')
    success_url = reverse_lazy('myblog:list')


class MyblogDetailView(DetailView):
    model = Myblog


class MyblogDeleteView(DeleteView):
    model = Myblog
    success_url = reverse_lazy('myblog:list')
