from django.shortcuts import render
from .models import *

def listaTarefas (request):
    tarefas = Tarefas.objects.all().order_by('-titulo')
    return render(request, 'list/listaTarefa.html', {'tarefas' : tarefas})

# Create your views here.
