from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Todo
from django.views.generic import ListView, CreateView


# Create your views here.
class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
