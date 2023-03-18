from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    path('file-list', views.file_list, name='file-list'),
    path('<int:id>/', views.file_detail, name='file-detail'),
    path('file/upload', views.file_upload, name='file-upload'),
    path('search-results', views.search_result, name='search-result'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('copyright', views.copyright, name='copyright'),
    path('terms-privacy', views.terms_privacy, name='terms-privacy')
]
