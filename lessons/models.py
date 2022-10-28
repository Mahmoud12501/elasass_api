from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Class(models.Model):
    name=models.CharField("Class_name",max_length=100,unique=True)
    slug=models.SlugField(max_length=100,blank=True,null=True,editable = False)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name) 
        super(Class,self).save(*args,**kwargs)
    
    def __str__(self) -> str:
        return self.name
    
class Subject(models.Model):
    name=models.CharField("Subject_name ",max_length=100,unique=True)
    describtion=models.TextField(max_length=1000)
    classe=models.ForeignKey(Class,verbose_name=("Classes"),related_name='class_subject',on_delete=models.CASCADE,null=True,blank=True)
    slug=models.SlugField(max_length=100,blank=True,null=True,editable = False)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name) 
        super(Subject,self).save(*args,**kwargs)
        
    def __str__(self) -> str:
        return self.name
    
class Playlist(models.Model):
    title=models.CharField(max_length=100,unique=True)
    playlist_link=models.URLField()
    subject=models.ForeignKey('Subject',verbose_name=("Subject"),related_name='playlist_subject',on_delete=models.CASCADE,null=True,blank=True)
    author=models.ForeignKey(User,verbose_name=("User"),related_name='author_playlist',on_delete=models.SET_NULL,null=True,blank=True)
    slug=models.SlugField(max_length=100,blank=True,null=True,editable = False)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title) 
        super(Playlist,self).save(*args,**kwargs)
        
    def __str__(self) -> str:
        return self.title
