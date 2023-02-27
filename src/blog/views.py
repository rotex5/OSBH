from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
# Create your views here.
from .forms import CommentForm
from .models import Blog


def list_blog(request):
    """Blog list view"""
    blog_list = Blog.objects.all()
    context = {
        'blog_list': blog_list
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, id):
    """Blog detail view"""
    blog = Blog.objects.get(id=id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/blog-detail.html', context)


def create_comment(request, id):
    """Comment view"""
    blog = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.commenter = request.user
            form.instance.blog = blog
            form.save()
        return redirect('blog-detail', id=id)
    else:
        form = CommentForm()
    context = {
        'blog': blog,
        'form': form
    }
    return render(request, 'blog/create-comment.html', context)
