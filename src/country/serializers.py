from rest_framework import serializers
from .models import Country
from .models import State
from .models import City
from .models import Urban

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'slug']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {
                'lookup_field': 'slug'
            }
        }

class StateSerializer(serializers.ModelSerializer):
    # country_id = CountrySerializer(many=True, read_only=True)
    class Meta:
        model = State
        fields = ['id', 'state_name', 'slug', 'country_id']
        lookup_field = 'slug'


class CitySerializer(serializers.ModelSerializer):
    # state_id = StateSerializer(many=True, read_only=True)
    class Meta:
        model = City
        fields = ['id', 'city_name', 'state_id']

class UrbanSerializer(serializers.ModelSerializer):
    # state_id = StateSerializer(many=True, read_only=True)
    class Meta:
        model = Urban
        fields = ['id', 'urban_name', 'state_id']
