from django.shortcuts import render

# Create your views here.
from .models import Blog


def list_blog(request):
    blog_list = Blog.objects.all()
    context = {
        'blog_list': blog_list
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/blog-detail.html', context)
