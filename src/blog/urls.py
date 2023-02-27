from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_blog, name='blogs'),
    path('<int:id>/', views.blog_detail, name='blog-detail'),
    path('<int:id>/create', views.create_comment, name='comment-create'),
    # path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:id>', views.author_detail, name='author-detail'),
    # path('comment/<int:pk>/', views.comment_create, name='comment-create'),
]
