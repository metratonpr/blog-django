from django.contrib import admin
from django.urls import path
from .views import lista_posts, detalhes_post


urlpatterns = [
    path("", lista_posts, name='lista_posts'),
    path("post/<int:pk>", detalhes_post, name='detalhes_post'),
    
]