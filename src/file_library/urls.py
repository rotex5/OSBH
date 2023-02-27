from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_list, name='file-list'),
    path('file/upload', views.file_upload, name='file-upload'),
]
