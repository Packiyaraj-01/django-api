from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/',
        'View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serialize = TaskSerializer(tasks,many=True)

    response = {
        'success': True,
        'message':'Task List',
        'list': serialize.data
    }
    return Response(response)

@api_view(['GET'])
def taskDetailView(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task,many=False)

    response = {
        'success': True,
        'message':'Task Detail View',
        'result': serializer.data
    }
    return Response(response)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Task Deleted Successfully')