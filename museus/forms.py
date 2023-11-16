from django.forms import ModelForm
from .models import Post


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