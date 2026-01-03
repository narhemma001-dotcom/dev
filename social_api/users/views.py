from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import User, FollowModel
from .serializers import RegisterSerializer, FollowSerializer,UserProfileSerializer

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RegisterSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
class FollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            to_follow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if to_follow == request.user:
            return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        
        follow_relation, created = FollowModel.objects.get_or_create(
            follower=request.user,
            following=to_follow
        )
        
        if created:
            request.user.following_count += 1
            to_follow.followers_count += 1
            request.user.save()
            to_follow.save()
            return Response({"message": "Successfully followed the user"}, status=status.HTTP_201_CREATED)
        else:
            follow_relation.delete()
            request.user.following_count -= 1
            to_follow.followers_count -= 1
            request.user.save()
            to_follow.save()
            return Response({"message": "Successfully unfollowed the user"}, status=status.HTTP_200_OK)  

class FollowersListView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request):
        user_followers = FollowModel.objects.filter(following=request.user)
        serializer = FollowSerializer(user_followers, many=True)
        return Response(serializer.data)
    
class FollowingListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_following = FollowModel.objects.filter(follower=request.user)
        serializer = FollowSerializer(user_following, many=True)
        return Response(serializer.data)