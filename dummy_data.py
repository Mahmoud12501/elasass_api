import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

############
from faker import Faker
import random
from lessons.models import Playlist,Class,Subject
from django.contrib.auth.models import User


def seek_class(n):
    fake=Faker()
    
    for _ in range(n):
        name=fake.name()
        
        Class.objects.create(
            name=name,
            slug='',
            
        )

def seek_subject(n):
    fake=Faker()
    
    
    for _ in range(n):
        name=fake.name()
        describtion=fake.text(max_nb_chars=1000)
        classs=Class.objects.get(id=random.randint(11,13))
       
        Subject.objects.create(
            name=name,
            describtion=describtion,
            classe=classs,
            slug='',
            
        )
        
def seek_playlist(n):
    fake=Faker()
    
    
    for _ in range(n):
        title=fake.name()
        playlist_link="https://youtube.com/playlist?list=PLCXxeGQt1gBzvQiuuMYVt0h_7ZnShGZxP"
        subject=Subject.objects.get(id=random.randint(7,13))
        author=User.objects.get(id=random.randint(1,2))
        Playlist.objects.create(
            title=title,
            playlist_link=playlist_link,
            subject=subject,
            author=author,
            slug='',
            
        )

# seek_class(3)
seek_subject(5)
seek_playlist(10)