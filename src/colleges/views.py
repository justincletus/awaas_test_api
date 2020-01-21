from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import status, generics, mixins, viewsets
from .models import College
from .serializers import CollegeSerializer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .sqliteReader import main
from university.models import University
from country.models import Country
from country.models import State
from country.models import City
from courses.models import Course

# Create your views here.

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    lookup_field = 'slug'

    def list(self, request, *args, **kwargs):

        university = get_object_or_404(University, id=3)

        country = get_object_or_404(Country, id=1)
        # print(country)
        state = get_object_or_404(State, id=130)
        # print(state)
        city = get_object_or_404(City, id=1357)
        # print(city)

        colleges = College.objects.all()

        course = get_object_or_404(Course, id=2)
        print(course)

        # for college in colleges:
        #     if college.college_name == '':
        #         # college_update = College(course_id=course)
        #         try:
        #             college.delete()
        #         except:
        #             print('some issue in delete.')

        # for college in colleges:
        #     college_update = College(graduate='Under Graduate', course_id=course)
        #
        # # college_list = main()
        # # for coll in college_list:
        # #     college_update = College(college_name=coll[2].replace("\n", ""), address=coll[3].replace("\n", ""), university_id=university)
        #     try:
        #         if college.college_name is None:
        #             college.delete()
        #     except:
        #         print('some issue in save data')

        serializer = CollegeSerializer(colleges, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def CollegesByUniversity(request, slug):
    try:
        university = University.objects.get(slug=slug)
        colleges = College.objects.filter(university_id=university).values('id', 'college_name', 'slug')

    except University.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        colleges = list(colleges.values())
        return JsonResponse(colleges, safe=False)
