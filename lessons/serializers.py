from rest_framework import serializers
from .models import Class,Playlist,Subject

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=Class
        fields='__all__' 
        # exclude = ('slug', )
        lookup_field='slug'
        extr_kwargs={
            'url':{'lookup_field':'slug'}
        }


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields='__all__'
        # exclude = ('slug', )
        
        lookup_field='slug'
        extr_kwargs={
            'url':{'lookup_field':'slug'}
        }

      
class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Playlist
        fields='__all__'
        # exclude = ('slug', )
        
        lookup_field='slug'
        extr_kwargs={
            'url':{'lookup_field':'slug'}
        }
        
