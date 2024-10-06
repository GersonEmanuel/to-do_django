
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TudoForm



# Create your views here.

def index(request):
    tarefas = Todo.objects.all()

    context = {'tarefas': tarefas}
    return render(request, 'todos/todo_list.html', context)

def cadastrar(request):
    form = TudoForm()
    if request.method == 'POST':
        form =TudoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'todos/todo_form.html', context)

