from rest_framework import serializers
from .models import Class,Playlist,Subject
from django.contrib.auth.models import User



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
    classe=ClassSerializer(many=False, read_only=True)
    class Meta:
        model=Subject
        fields='__all__'
        # exclude = ('slug', )
        
        lookup_field='slug'
        extr_kwargs={
            'url':{'lookup_field':'slug'}
        }

      
class PlaylistSerializer(serializers.ModelSerializer):
    subject=SubjectSerializer(many=False, read_only=True)
    # subject=serializers.StringRelatedField(many=False,read_only=False)
    class Meta:
        model=Playlist
        fields='__all__'
        # exclude = ('slug', )
        
        lookup_field='slug'
        extr_kwargs={
            'url':{'lookup_field':'slug'}
        }
        




class SubjectSerializer2(serializers.ModelSerializer):
    
    class Meta:
        model=Subject
        fields='__all__'
        # exclude = ('slug', )
        
        lookup_field='slug'
        extr_kwargs={
            'url':{'lookup_field':'slug'}
        }

      
class PlaylistSerializer2(serializers.ModelSerializer):
    
    class Meta:
        model=Playlist
        fields='__all__'
        # exclude = ('slug', )
        
        lookup_field='slug'
        extr_kwargs={
            'url':{'lookup_field':'slug'}
        }