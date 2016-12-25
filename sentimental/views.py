from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects
    return render(request, 'sentimental/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            return render(request, 'sentimental/post_list.html', {'post': post})
    else:
        form = PostForm()
    return render(request, 'sentimental/post_edit.html', {'form': form})
