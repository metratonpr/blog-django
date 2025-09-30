from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm

# Create your views here.
def lista_posts(request):
    posts = Post.objects.all().order_by('-data_criacao')
    return render(request, 'blog/lista_posts.html',{'posts': posts})

def detalhes_post(request, pk):
    post = get_object_or_404(Post,pk=pk)

    # filtrar os comentarios
    comments = post.comments.filter(ativo=True)

    # novo comentario
    novo_comentario = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            novo_comentario = comment_form.save(commit=False)
            novo_comentario.post = post
            novo_comentario.save()
            novo_comentario = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/detalhes_post.html',{
        'post': post,
        'comments': comments,
        'novo_comentario': novo_comentario,
        'comment_form' : comment_form
    })