from django.contrib import admin
from .models import Playlist,Subject,Class
# Register your models here.
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Playlist)
