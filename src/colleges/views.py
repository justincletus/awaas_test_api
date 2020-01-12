from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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

# Create your views here.

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

    def list(self, request, *args, **kwargs):

        university = get_object_or_404(University, id=3)

        country = get_object_or_404(Country, id=1)
        # print(country)
        state = get_object_or_404(State, id=130)
        # print(state)
        city = get_object_or_404(City, id=1357)
        # print(city)

        colleges = College.objects.all()

        # college_list = main()
        # for coll in college_list:
        #     college_update = College(college_name=coll[2].replace("\n", ""), address=coll[3].replace("\n", ""), university_id=university)
        #     try:
        #         college_update.save()
        #     except:
        #         print('some issue in save data')

        serializer = CollegeSerializer(colleges, many=True)
        return Response(serializer.data)
