from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_blog, name='blogs'),
    path('<int:id>/', views.blog_detail, name='blog-detail'),
    # path('<int:pk>/create', views.CommentCreateView.as_view(),
    #     name='comment-create'),
    # path('authors/', views.AuthorListView.as_view(), name='authors'),
    # path('author/<int:pk>', views.AuthorDetailsView.as_view(),
    #     name='author-detail'),
    # path('comment/<int:pk>/', views.comment_create, name='comment-create'),
]
