from django.shortcuts import render
from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course
from university.models import University
# from ..university.models import University
from colleges.models import College
from .serializers import CourseSerializer
from university.serializers import UniversitySerializer
from colleges.serializers import CollegeSerializer


@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(
            courses,
            context={
                'request': request
            },
            many=True
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(
            course,
            context={
                'request': request
            }
        )
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CourseSerializer(
            course,
            data=request.data,
            context={
                'request': request
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

