from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Class,Playlist,Subject
from .serializers import ClassSerializer,PlaylistSerializer,SubjectSerializer
# Create your views here.

class ClassViewsets(viewsets.ModelViewSet):
    queryset=Class.objects.all()
    serializer_class=ClassSerializer
    lookup_field='slug'
    
class PlaylistViewsets(viewsets.ModelViewSet):
    queryset=Playlist.objects.all()
    serializer_class=PlaylistSerializer
    lookup_field='slug'
    
class SubjectViewsets(viewsets.ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer
    lookup_field='slug'