from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, generics, mixins, viewsets
from .models import College
from .serializers import CollegeSerializer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Create your views here.

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

    def list(self, request, *args, **kwargs):
        college = College.objects.all()
        serializer = CollegeSerializer(college, many=True)
        return Response(serializer.data)