from django.urls import path
from .views import PostModelListCreateAPIView, PostModelDetailAPIView

urlpatterns = [
    path('posts/', PostModelListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostModelDetailAPIView.as_view(), name= 'post-detail'),
]