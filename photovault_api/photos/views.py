from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db import models
from .models import Photo
from .serializers import PhotoSerializer

# Custom permission: Only owner can edit/delete
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for owner
        return obj.owner == request.user

# Upload/Create photo
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def upload_photo(request):
    serializer = PhotoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)  # Set owner to current user
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List photos (public + user's private)
@api_view(['GET'])
def list_photos(request):
    if request.user.is_authenticated:
        # Show public photos + user's private photos
        photos = Photo.objects.filter(
            models.Q(visibility='public') | 
            models.Q(owner=request.user, visibility='private')
        )
    else:
        # Show only public photos for non-authenticated users
        photos = Photo.objects.filter(visibility='public')
    
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)

# Photo detail, update, delete
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([permissions.IsAuthenticated, IsOwnerOrReadOnly])
def photo_detail(request, pk):
    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)
    
    elif request.method in ['PUT', 'PATCH']:
        serializer = PhotoSerializer(photo, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)