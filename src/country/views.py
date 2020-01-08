from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, generics, status
from .models import Country
from .models import State
from .models import City
from .models import Urban
from .serializers import CountrySerializer
from .serializers import StateSerializer
from .serializers import CitySerializer
from .serializers import UrbanSerializer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import csv, io
from django.templatetags.static import static
from django.core.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import DestroyAPIView, UpdateAPIView, RetrieveAPIView
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

# Create your views here.

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def list(self, request, *args, **kwargs):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def list(self, request, *args, **kwargs):
        state = State.objects.all()

        csv_details = open('/Users/justincletus/djangoDev/smartuniv/src/static/other_files/india-state-city-urban.csv', 'r')
        if not csv_details.name.endswith('.csv'):
            raise ValidationError('Invalid file type')
        try:
            csvdata = csv.reader(csv_details)
            counter = 0
            state_counter = 0
            filter_out = []
            for row in csvdata:
                for res in state:
                    if res.state_name == row[1]:
                        # state_csv = Urban(urban_name=row[2].strip(), state_id=res.id)
                        # try:
                        #     state_csv.save()
                        # except:
                        #     print("Some issue in saving data")
                        # out = 'insert into country_city(city_name, state_id_id) values(', row[0].strip(), res.id, ")"
                        # filter_out.append(out)
                        #print('insert into country_city(city_name, state_id_id) values(' ,"'" ,row[0].strip() ,"'" ,res.id ,")")
                        counter = counter + 1

            print(counter)

            for resp in filter_out:
                print(resp, '\n')

        except csv.Error:
            raise ValidationError('failed to read the file')

        # for row in state:
        #     print(row.id ,'\n')
        serializer = StateSerializer(state, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        c_id = self.kwargs.get('pk', None)
        if c_id is not None:
            states = get_object_or_404(State, country_id=c_id)
            return State.objects.filter(

            )
        else:
            return State.objects.none()

class StateDestroyView(DestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateUpdateView(UpdateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateDetailsView(RetrieveAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


    # def get_queryset(self):
    #     c_id = self.request.query_params.get('country_id')
    #     objects = get_object_or_404(State, country_id=c_id)
    #
    #     serializer = StateSerializer(objects, many=True)
    #     return Response(serializer.data)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def list(self, request, *args, **kwargs):
        city = City.objects.all()
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data)


class UrbanViewSet(viewsets.ModelViewSet):
    queryset = Urban.objects.all()
    serializer_class = UrbanSerializer

    def list(self, request, *args, **kwargs):
        urban = Urban.objects.all()
        serializer = UrbanSerializer(urban, many=True)
        return Response(serializer.data)


class StateByCountryViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def list(self, request, *args, **kwargs):
        state = State.objects.all()
        serializer = StateSerializer(state)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = State.objects.all()
    #     pk = 1
    #
    #     states = get_object_or_404(queryset, pk=pk)
    #     serializer = StateSerializer(states)
    #     return Response(serializer.data)

    # serializer_class = StateSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['country_id']

    # def get_queryset(self):
    #     country_id = 1
    #     objects = get_object_or_404(State, country_id=country_id)
    #     serializer = StateSerializer(objects, many=True)
    #     return Response(serializer.data)


# def StateByCountry_view(request):
#     queryset = State.objects.all()
#
#     return Response('abcd')

@api_view(['GET'])
def StateByCountry(request, pk):
    try:
        state_list = State.objects.filter(country_id=pk).values('id', 'state_name', 'country_id')
        # print(list(state_list))
        # json_dump(state_list)
        # return HttpResponse(list(state_list))

    except State.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        states = list(state_list.values())
        return JsonResponse(states, safe=False)
        # qs_json = serializers.serialize('json', states)
        # return HttpResponse(qs_json, content_type='application/json')

        # serializer = StateSerializer(states)
        # return Response(serializer.data)

