from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import User
from .serializer import UserSerializer

# Create your views here.
def home (request):
    return HttpResponse ('<h1> Alessio Portfolio Project DevOps <h1>')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer