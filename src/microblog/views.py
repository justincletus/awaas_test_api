from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .models import BlogPost
from . import serializers
from .serializers import BlogPostSerializer
from .permissions import ReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (ReadOnly,)

def index(request, path=''):
    return render(request, 'index.html')

class BlogPostViewSet(viewsets.ModelViewSet):

    #Provides basic CRUD functions for the Blog Post Model
    queryset = BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer
    permissions_class = (permissions.IsAuthenticatedOrReadOnly,)


    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World'}
        return Response(content)

