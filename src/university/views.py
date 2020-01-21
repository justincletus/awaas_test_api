from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status, generics, mixins
from .models import University
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import UniversitySerializer
from country.models import State

# Create your views here.

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    lookup_field = 'slug'

    def list(self, request, *args, **kwargs):
        university = University.objects.all()
        serializer = UniversitySerializer(university, many=True)
        return Response(serializer.data)

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)


@api_view(['GET'])
def StateByUniversity(request, slug):
    try:
        state = State.objects.get(slug=slug)
        universities = University.objects.filter(state_id=state).values('id', 'name', 'slug')

    except State.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        unniversity = list(universities.values())
        return JsonResponse(unniversity, safe=False)
