from django.db import models 

class Postagem (models.Model):
    titulo = models.CharField(max_length=200) #com de até 500 caracteres
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True) #utiliza a data e hora do sistema

    def __str__(self):
        return self.titulo