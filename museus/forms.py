from django.forms import ModelForm
from .models import Post, Comment



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'text',
            'poster_url',
        ]
        labels = {
            'name': 'Título',
            'text': 'Descrição',
            'poster_url': 'Foto do Museu',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }