from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Todo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from datetime import *


# Create your views here.
class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')

class TodoCompleteView(View):
    def get(self, request, pk):
#        Todo.objects.get(pk = pk)
        todo = get_object_or_404(Todo, pk=pk)
        todo.finished_data = date.today()
        todo.save()
        return redirect("todo_list")

