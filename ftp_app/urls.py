from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('upload/', views.upload_file, name='upload'),
    path('download/<str:filename>/', views.download_file, name='download_file'),
]