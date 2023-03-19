from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.utils.timesince import timesince
from django.shortcuts import render, get_object_or_404, redirect
from .models import Forum, Discussion
from .forms import ForumForm
# Create your views here.

def list_forum(request):
    forums = Forum.objects.all()
    context = {
        'forums': forums
    }
    return render(request, 'forum/forum-list.html', context)


def forum_create(request):
    """create a Forum"""
    form = ForumForm()
    if request.method == "POST":
        form = ForumForm(request.POST)
        if form.is_valid():
            creator = get_object_or_404(User, user=request.user)
            form.instance.creator =  creator   
            form.save()
            id= form.instance.id
            return redirect('forum-detail', id=id)
    context = {
        'form': form
    }
    return render(request, 'forum/forum-create.html', context)


def forum_detail(request, id):
    forum = get_object_or_404(Forum, id=id)
    context = {
        'forum': forum
    }
    return render(request, 'forum/forum-detail.html', context)


def getMessages(request, id):
    forum = Forum.objects.get(id=id)
    messages = Discussion.objects.filter(forum=forum )
    return JsonResponse({"messages":list(messages.values(
        'forum',
        'forum__topic',
        'message',
        'commenter',
        'commenter__username',
        'timestamp'
        ))})


def send(request, id):
    forum = get_object_or_404(Forum, id=id)
    message = request.POST['message']
    commenter = request.user

    new_message = Discussion.objects.create(forum=forum, message=message, commenter=commenter)
    new_message.save()
    return HttpResponse('Message sent successfully')


def forum_delete(request, id):
    """delete a forum"""
    forum = get_object_or_404(Forum, id=id)
    forum.delete()
    return redirect('forums')
