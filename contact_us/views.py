from django.shortcuts import render
from rest_framework import viewsets
from .models import ContactUs
from .serializars import ContactUsserializers

# Create your views here.

# ModelViewSet akta khub power full view set amra aikhane (post,get,put,delete) korte parbo

class ContactUsViewSet(viewsets.ModelViewSet):
        queryset = ContactUs.objects.all()
        serializer_class = ContactUsserializers