from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Taskmodel
from .serializers import TaskSerializer

@api_view(['GET'])
def task_list(request):
    # GET list never returns 404 for empty database
    tasks = Taskmodel.objects.all()
    serializer = TaskSerializer(tasks, many=True)  # ← many=True for lists
    return Response(serializer.data)

@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)  # ← data= parameter
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # ← return errors

@api_view(['GET'])
def task_detail(request, pk):
    try:
        task = Taskmodel.objects.get(id=pk)
        serializer = TaskSerializer(task)  # ← No many=True for single object
        return Response(serializer.data)
    except Taskmodel.DoesNotExist:  # ← Fixed spelling
        return Response(
            {'message': 'Task not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['PUT'])
def task_update(request, pk):
    try:
        task = Taskmodel.objects.get(id=pk)
        serializer = TaskSerializer(task, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Taskmodel.DoesNotExist:
        return Response(
            {'message': 'Task not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['DELETE'])
def task_delete(request, pk):
    try:
        task = Taskmodel.objects.get(id=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  # ← No message with 204
    
    except Taskmodel.DoesNotExist:
        return Response(
            {'message': 'Task not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )