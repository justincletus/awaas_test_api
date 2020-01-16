from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    # slug = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    # )
    class Meta:
        model = Category
        fields =['id', 'name', 'slug']
