from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_forum, name='forums'),
    path('create', views.forum_create, name='forum-create'),
    path('<int:id>', views.forum_detail, name='forum-detail'),
    path('<int:id>/getMessages', views.getMessages, name='getMessages'),
    path('<int:id>/send', views.send, name='send'),
    path('<int:id>/delete', views.forum_delete, name='forum-delete'),
]
