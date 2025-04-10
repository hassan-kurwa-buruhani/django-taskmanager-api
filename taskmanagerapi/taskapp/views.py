from django.shortcuts import render
from .models import Profile, Tag, Task
from .serializers import *
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


User = get_user_model()

# Create your views here.
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# @permission_classes(IsAuthenticated)
def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'DELETE', 'PUT']) 
    

    def api(request, id=None):
        if request.method == 'GET':
            if id:
                try:
                    instance =model_class.objects.get(id=id)
                    serializer = serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'})
            else:
                instance = model_class.objects.all()
                serializer = serializer_class(instance, many=True)
                return Response(serializer.data)
        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            user = request.user
            if id:
                try:
                    instance =model_class.objects.get(id=id)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save(lecturer=user)
                        
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'})
                
        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    instance.delete()
                    return Response({'message': 'Deleted successfully'})
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'})
    return api

manage_users = generic_api(User, UserSerializer)
manage_tasks = generic_api(Task, TaskSerializer)
manage_tags = generic_api(Tag, TagSerializer)
manage_profiles = generic_api(Profile, ProfileSerializer)



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_task_count(request):
    task_count = Task.objects.all().count()
    return Response({'task_count': task_count})

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_overdue_tasks(request):
    overdue_tasks = Task.objects.filter(due_date__lt=timezone.now())
    serializer = TaskSerializer(overdue_tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_completed_tasks(request):
    completed_tasks = Task.objects.filter(is_completed=True)
    serializer = TaskSerializer(completed_tasks, many=True)
    return Response(serializer.data)

    
   