from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    all_posts = Post.newmanager.all()
    ordering = '-publish'
    return render(request, 'index.html', {'posts': all_posts})


def post_single(request, post):
    post = post.get_object_or_404(Post, slug=post, status='published')
    return render(request, 'single.html', {'post': post})
