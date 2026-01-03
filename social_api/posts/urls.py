from django.urls import path
from .views import PostListView, PostDetailView, CommentListView,LikeView


urlpatterns = [
    path('', PostListView.as_view(), name='post-list-create'),
    path('<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_id>/comments/', CommentListView.as_view(), name='comment-list-create'),
    path('<int:post_id>/like/', LikeView.as_view(), name='like-list-create'),
]
    