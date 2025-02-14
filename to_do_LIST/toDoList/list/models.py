from django.db import models

# Create your models here.

class Tarefas (models.Model) :
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    status = models.BooleanField()