from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
from .forms import BlogForm, CommentForm
from .models import Blog, BlogAuthor, BlogLike, BlogView


def list_blog(request):
    """Blog list view"""
    blog_list = Blog.objects.all()
    context = {
        'blog_list': blog_list
    }
    return render(request, 'blog/blog-list.html', context)


# @login_required
def blog_create(request):
    """posting a blog"""
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            author = get_object_or_404(BlogAuthor, user=request.user)
            form.instance.author =  author    
            form.save()
            id= form.instance.id
            return redirect('blog-detail', id=id)
            # return redirect('blogs')
    context = {
        'form': form
    }
    return render(request, 'blog/blog-create.html', context)


def blog_detail(request, id):
    # Comment view
    blog = get_object_or_404(Blog, id=id)
    if request.user.is_authenticated:
        BlogView.objects.get_or_create(user=request.user, blog=blog)
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
    return render(request, 'blog/blog-detail.html', context)


def blog_update(request, id):
    """update a blog"""
    blog = get_object_or_404(Blog, id=id)
    form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
    if form.is_valid():
        author = get_object_or_404(BlogAuthor, user=request.user)
        form.instance.author =  author    
        form.save()
        return redirect('blog-detail', id=id)
    context = {
        'form': form,
        'blog': blog
    }
    return render(request, 'blog/blog-update.html', context)


def blog_delete(request, id):
    """delete a blog"""
    blog = get_object_or_404(Blog, id=id)
    blog.delete()
    return redirect('blogs')


def author_detail(request, id):
    """View showing the details of an author"""
    author = BlogAuthor.objects.get(id=id)
    context = {
        'author': author
    }
    return render(request, 'blog/author-detail.html', context)


def blog_like(request, id):
    """Like associated with a blog instance"""
    blog = get_object_or_404(Blog, id=id)
    like = BlogLike.objects.filter(user=request.user, post=blog)
    if like.exists():
        like[0].delete()
        return redirect('blog-detail', id=id)
    BlogLike.objects.create(user=request.user, post=blog)
    return redirect('blog-detail', id=id)

