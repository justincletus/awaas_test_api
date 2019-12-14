from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer, ContactMiniSerializer
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .forms import ContactForm


@method_decorator(csrf_exempt, name='dispatch')
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def list(self, request, *args, **kwargs):
        contacts = Contact.objects.all()
        serializer = ContactMiniSerializer(contacts, many=True)
        return Response(serializer.data)
