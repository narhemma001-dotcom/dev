from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_photo, name='upload_photo'),
    path('', views.list_photos, name='list_photos'),
    path('<int:pk>/', views.photo_detail, name='photo_detail'),
]