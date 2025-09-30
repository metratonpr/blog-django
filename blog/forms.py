from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['nome', 'email', 'corpo']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border border-slate-300 shadow-sm p-3 focus:border-blue-500 focus:ring focus:ring-blue-200',
                'placeholder': 'Digite seu nome'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'mt-1 block w-full rounded-md border border-slate-300 shadow-sm p-3 focus:border-blue-500 focus:ring focus:ring-blue-200',
                'placeholder': 'Digite seu e-mail'
            }),
            'corpo': forms.Textarea(attrs={
                'class': 'mt-1 block w-full rounded-md border border-slate-300 shadow-sm p-3 focus:border-blue-500 focus:ring focus:ring-blue-200',
                'placeholder': 'Escreva seu comentário...',
                'rows': 4
            }),
        }
