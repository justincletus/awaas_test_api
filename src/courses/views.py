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
from category.csvReader import main
from category.models import Category


@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all() # function
        category = Category.objects.all()
        course_cat = [] # square bracket
        for cat in category:
            # print(cat.name)
            course_cat.append(cat)

        # print(course_cat[0])

        course_list = main()
        # print(course_list)

        abcd  = course_list["FACULTY OF ARTS"]
        abcd  = abcd.dropna(how='any', axis=0)

        cd = []
        for ab in abcd:
            cd.append(ab.split(','))

        acron = []
        for c in cd:
            acron.append(".".join(e[0] for e in c[0].split() if e[0].isupper()))

        for i in range(len(cd)):
            # course_update = Course(course_name=cd[i][0], course_sn=acron[i], course_year='3', category=course_cat[0])

            print(cd[i][0], acron[i])

            # try:
            #     course_update.save()
            # except:
            #     print('Some issue in save course')


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
        if serializer.is_valid(): # serializer valid condition
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
