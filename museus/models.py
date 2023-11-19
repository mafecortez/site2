from django.db import models
from django.conf import settings


class Post(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    poster_url = models.URLField(max_length=200, null=True)
    post_date = models.DateTimeField(auto_now_add=True)  


    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    post_date = models.DateTimeField(auto_now_add=True) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField() 
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return f'{self.name}'