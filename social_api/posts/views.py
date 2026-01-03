from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import PostModel, CommentModel, LikeModel
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from . import permissions as post_permissions

class PostListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        posts = PostModel.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated,  post_permissions.IsOwnerOrReadOnly]

    def get_object(self, post_id):
        try:
            return PostModel.objects.get(id=post_id)
        except PostModel.DoesNotExist:
            return None

    def get(self, request, post_id):
        post = self.get_object(post_id)   
        if not post:
            return Response(
                {"error": "Post not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )           
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, post_id):
        post = self.get_object(post_id)
        if not post:
            return Response(
                {"error": "Post not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        if not request.user == post.owner:  
            return Response(
                {"error": "You do not have permission to edit this post"}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           
    def delete(self, request, post_id):
        post = self.get_object(post_id)
        if request.user == post.owner:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)            
        return Response({"error": "You do not have permission to delete this post"}, status=status.HTTP_403_FORBIDDEN)
        


class CommentListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, post_id):
        comments = CommentModel.objects.filter(id=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, post_id):
        try:
            post = PostModel.objects.get(id=post_id)
        except PostModel.DoesNotExist:
            return Response(
                {"error": "Post not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )        
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user, post_id=post_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = PostModel.objects.get(id = post_id)
        like, created = LikeModel.objects.get_or_create(owner=request.user, post= post)
        if created:
            post.likes_count += 1
            post.save()
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        else:
            like.delete()
            post.likes_count -= 1
            post.save()
            return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)    
