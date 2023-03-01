from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.
from .forms import FileForm
from .models import File, FileUploader


def file_list(request):
    files = File.objects.all()
    uploader = None
    try:
        uploader = FileUploader.objects.get(user = request.user)
    except Exception:
        pass
    context = {
        'files': files,
        'uploader': uploader
    }
    return render(request, 'file_library/file_list.html', context)
 

@login_required
def file_upload(request):
    user = FileUploader.objects.get(user = request.user)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.uploader = user
            form.save()
            if user.has_uploaded is False:
                user.has_uploaded = True
                user.save()
            return redirect('file-list')
    else:
        form = FileForm()

    context = {
        'form': form
    }
    return render(request, 'file_library/upload.html', context)
