from django.shortcuts import render


# Create your views here.
def todo_list(request):
    nome = 'Gerson'
    matriz = [[i for i in range(3)] for i in range(3)]
    return render(request, "todos/todo_list.html", {'nome': nome, 'matriz': matriz})
