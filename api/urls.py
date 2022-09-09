from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='home'),
    path('api/all_videos', views.all_videos, name='api_all_videos')
]
