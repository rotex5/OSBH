from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.utils.timesince import timesince
from django.shortcuts import render, get_object_or_404, redirect

from .forms import DiscussionForm, ThreadForm
from .models import Thread

# Create your views here.

def list_thread(request):
    """List all available threads"""
    threads = Thread.objects.all()
    context = {
        'threads': threads
    }
    return render(request, 'forum/thread-list.html', context)


def thread_detail(request, id):
    """View the details of a thread"""
    thread = get_object_or_404(Thread, id=id)
    
    if request.method == "POST":
        form = DiscussionForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.thread = thread
            form.save()
        return redirect('thread-detail', id=id)
    else:
        form = DiscussionForm()


    context = {
        'form': form,
        'thread': thread
    }
    return render(request, 'forum/thread-detail.html', context)

def thread_create(request):
    """creating a thread"""
    form = ThreadForm()
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            author = get_object_or_404(User, username=request.user)
            form.instance.author =  author    
            form.save()
            id= form.instance.id
            return redirect('thread-detail', id=id)
    context = {
        'form': form
    }
    return render(request, 'forum/thread-create.html', context)

