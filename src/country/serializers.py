from rest_framework import serializers
from .models import Country
from .models import State
from .models import City
from .models import Urban

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'slug']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'state_name']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_name']

class UrbanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urban
        fields = ['id', 'urban_name']