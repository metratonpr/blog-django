from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('detalhe_post', args=[str(self.id)])
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments' )
    nome = models.CharField(max_length=80)
    email = models.EmailField()
    corpo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return f'Comentario de {self.nome} em {self.post}'

