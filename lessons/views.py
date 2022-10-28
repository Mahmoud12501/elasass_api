from django.shortcuts import render
from rest_framework import viewsets,status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Class,Playlist,Subject
from .serializers import ClassSerializer,PlaylistSerializer,SubjectSerializer,PlaylistSerializer2,SubjectSerializer2
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly ,IsAuthenticatedOrReadOnly,IsAdminUser,AllowAny
from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class ClassViewsets(viewsets.ModelViewSet):
    queryset=Class.objects.all()
    serializer_class=ClassSerializer
    lookup_field='slug'
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['name']
        
 
class SubjectViewsets(viewsets.ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer
    lookup_field='slug'
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['name']   
    
class AddSubject(generics.CreateAPIView):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer2
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
class EditSubject(generics.RetrieveUpdateDestroyAPIView):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer2
    lookup_field='slug'
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
class PlaylistViewsets(viewsets.ModelViewSet):
    queryset=Playlist.objects.all()
    serializer_class=PlaylistSerializer
    lookup_field='slug'
    permission_classes=[IsAuthorOrReadOnly,IsAuthenticatedOrReadOnly]
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['title','subject','author']
    
class AddPlay(generics.CreateAPIView):
    queryset=Playlist.objects.all()
    serializer_class=PlaylistSerializer2
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]    



class EditPlaylist(generics.RetrieveUpdateDestroyAPIView):
    queryset=Playlist.objects.all()
    serializer_class=PlaylistSerializer2
    permission_classes=[IsAuthorOrReadOnly,IsAuthenticatedOrReadOnly]
    lookup_field='slug'