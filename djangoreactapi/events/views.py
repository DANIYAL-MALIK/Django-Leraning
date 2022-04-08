from django.shortcuts import render
from .models import Events
from .serializers import LeadSerializer
from rest_framework import generics
# Create your views here.
class LeadListCreate(generics.ListCreateAPIView):
    queryset=Events.objects.all()
    serializer_class=LeadSerializer
