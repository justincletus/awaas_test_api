from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from rest_framework import viewsets, status
from django.template import RequestContext
from .forms import ProjectForm
from .models import Project, Task
from .serializers import ProjectSerializer, ProjectMiniSerializer, TaskSerializer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


@method_decorator(csrf_exempt, name='dispatch')
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectMiniSerializer(projects, many=True)
        return Response(serializer.data)

@method_decorator(csrf_exempt, name='dispatch')
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def taskById(request, pk):
    try:
        data = Task.objects.filter(project=pk).values('id', 'project', 'user', 'title', 'description', 'date')
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        tasks = list(data.values())
        return JsonResponse(tasks, safe=False)
