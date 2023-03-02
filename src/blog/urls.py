from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_blog, name='blogs'),
    path('create', views.blog_post, name='blog-post'),
    path('<int:id>/', views.blog_detail, name='blog-detail'),
    path('<int:id>/update', views.blog_update, name='blog-update'),
    path('author/<int:id>', views.author_detail, name='author-detail'),
]
