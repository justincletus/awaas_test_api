from rest_framework import serializers
from .models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'user', 'title', 'description', 'duration', 'date')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'project', 'user', 'title', 'description', 'start_date', 'end_date', 'date')

class ProjectMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'user', 'title', 'description', 'date')


