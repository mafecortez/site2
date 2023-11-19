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
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm

class PostListView(generic.ListView):
    model = Post
    template_name = 'museus/index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'museus/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object).order_by('-post_date')
        context['comment_form'] = CommentForm()
        return context

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
    
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('museus:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'museus/comment.html', context)

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'museus/list.html'


class CategoryCreateView(generic.CreateView):
    model = Category
    template_name = 'museus/create_list.html'
    fields = ['name', 'author', 'posts']
    success_url = reverse_lazy('museus:lists')
