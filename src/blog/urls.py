from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_blog, name='blogs'),
    path('create', views.blog_create, name='blog-create'),
    path('<int:id>/', views.blog_detail, name='blog-detail'),
    path('<int:id>/update', views.blog_update, name='blog-update'),
    path('<int:id>/delete', views.blog_delete, name='blog-delete'),
    path('author/<int:id>', views.author_detail, name='author-detail'),
    path('like/<int:id>/', views.blog_like, name='blog-like'),
]
