#from django.core.exceptions import ObjectDoesNotExist
#from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.
from .forms import FileForm
from .models import File, FileUploader
from blog.models import  Blog


def file_list(request):
    files = File.objects.all()
    context = {
        'files': files
    }
    return render(request, 'file_library/file_list.html', context)

def file_detail(request, id):
    file = get_object_or_404(File, id=id)
    uploader = None
    try:
        uploader = FileUploader.objects.get(user = request.user)
    except Exception:
        pass
    context = {
        'file': file,
        'uploader': uploader
    }
    return render(request, 'file_library/file-detail.html', context)
 

# @login_required
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

def search_result(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        file_results = File.objects.filter(title__icontains=searched)
        blog_results = Blog.objects.filter(title__icontains=searched)
        context = {
            'searched': searched,
            'file_results': file_results,
            'blog_results': blog_results
        } 
        return render(request, 'search-result.html', context)
    else:
        context = {}
        return render(request, 'search-result.html', context)
        
