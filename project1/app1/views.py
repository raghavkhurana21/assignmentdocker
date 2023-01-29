from django.shortcuts import render
from .models import Student
from .serializer import StudenrSerializer
from rest_framework import viewsets

# Create your views here.                               (we write our logics/functionality for what we want our project to do )
class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudenrSerializer