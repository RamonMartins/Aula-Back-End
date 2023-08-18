from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    concluida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
