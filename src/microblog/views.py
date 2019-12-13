from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import ReadOnly

# Create your views here.

def index(request, path=''):
    return render(request, 'index.html')

class BlogPostViewSet(viewsets.ModelViewSet):

    #Provides basic CRUD functions for the Blog Post Model
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permissions_class = (permissions.IsAuthenticatedOrReadOnly,)


    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

