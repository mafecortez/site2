from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.views import generic
from django.urls import reverse_lazy

class PostListView(generic.ListView):
    model = Post
    template_name = 'museus/index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'museus/detail.html'

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(name__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'museus/search.html', context)

class PostCreateView(generic.CreateView):
    model = Post
    fields = ["name", "text", "poster_url"]
    template_name = 'museus/create.html'
    success_url = reverse_lazy('museus:index')

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = ["name", "text", "poster_url"]
    template_name = 'museus/update.html'
    success_url = reverse_lazy('museus:index')

class PostDeleteView(generic.DeleteView):
    model = Post
    fields = ["name", "text", "poster_url"]
    template_name = 'museus/delete.html'
    success_url = reverse_lazy('museus:index')
