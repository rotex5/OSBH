from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_thread, name='forum'),
    path('<int:id>', views.thread_detail, name='thread-detail'),
    path('create', views.thread_create, name='thread-create'),
]
