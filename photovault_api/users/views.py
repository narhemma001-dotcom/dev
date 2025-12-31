from rest_framework.decorators import api_view, permission_classes
from .serializers import UserRegisterSerializer, UserProfileserializer
from rest_framework.response import Response
from rest_framework import permissions

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def RegisterView(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully"}, status=201)
    return Response(serializer.errors, status=400)
    

@api_view(['GET','PATCH'])
@permission_classes([permissions.IsAuthenticated])
def ProfileView(request):
    if request.method == 'GET':
        user = request.user
        serializer = UserProfileserializer(user)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        user = request.user
        serializer = UserProfileserializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    


    
