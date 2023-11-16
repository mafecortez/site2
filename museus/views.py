from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'museus/detail.html', context)

def list_posts(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'museus/index.html', context)

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(name__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'museus/search.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_name = form.cleaned_data['name']
            post_text = form.cleaned_data['text']
            post_poster_url = form.cleaned_data['poster_url']
            post = Post(name=post_name,
                          text=post_text,
                          poster_url=post_poster_url)
            post.save()
            return HttpResponseRedirect(
                reverse('museus:detail', args=(post.id, )))
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'museus/create.html', context)

def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post.name = form.cleaned_data['name']
            post.text = form.cleaned_data['text']
            post.poster_url = form.cleaned_data['poster_url']
            post.save()
            return HttpResponseRedirect(
                reverse('museus:detail', args=(post.id, )))
    else:
        form = PostForm(
            initial={
                'name': post.name,
                'text': post.text,
                'poster_url': post.poster_url
            })

    context = {'post': post, 'form': form}
    return render(request, 'museus/update.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('museus:index'))

    context = {'post': post}
    return render(request, 'museus/delete.html', context)