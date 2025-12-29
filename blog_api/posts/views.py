from rest_framework import generics, permissions
from .models import PostModel
from .serializers import PostModelSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PostModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 

    def perform_create(self, serializer):
        serializer.save(author= self.request.user)

class PostModelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
