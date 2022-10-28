from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter



app_name='lessons'
router=DefaultRouter()
router.register('classes',views.ClassViewsets)
router.register('subjects',views.SubjectViewsets)
router.register('classes/subjects/playlists',views.PlaylistViewsets)



urlpatterns = [
    
    path('api/',include(router.urls)),
    path('api/subject',views.AddSubject.as_view()),
    path('api/subject/<str:slug>',views.EditSubject.as_view()),
    path('api/add_playlist',views.AddPlay.as_view()),
    path('api/subject/playlist/<str:slug>',views.EditPlaylist.as_view()),
   
    
    
]