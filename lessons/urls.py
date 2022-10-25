from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter



app_name='lessons'
router=DefaultRouter()
router.register('classes',views.ClassViewsets)
router.register('subjects',views.SubjectViewsets)
router.register('playlists',views.PlaylistViewsets)


urlpatterns = [
    
    path('api/',include(router.urls)),
    
]