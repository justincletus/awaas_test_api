from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
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

