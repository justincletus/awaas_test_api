from django.shortcuts import render, get_object_or_404
from .models import Category
from rest_framework import status, generics, viewsets
from .serializers import CategorySerializer
from rest_framework.response import Response
from .csvReader import main

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        # cat_data = request.data
        # print(cat_data)
        categories = Category.objects.all()
        # serializer = self.get_serializer(cat_data)
        # print(serializer)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)

        # data_list = main()
        # for item in data_list:
        #     cat = Category(name=item.capitalize())
        #
        #     try:
        #         cat.save()
        #     except:
        #         print('Some issue in store category')

        serializer = CategorySerializer(categories, many=True)
        # self.perform_create(serializer)
        #return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.data)


    # def perform_create(self, serializer):
    #     serializer.save()
        # print('hello')
        # print(serializer)
