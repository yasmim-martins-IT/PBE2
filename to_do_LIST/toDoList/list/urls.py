from django.urls import path
from . import views

urlpatterns = [path('',views.listaTarefas, name = 'listaTarefa'),]