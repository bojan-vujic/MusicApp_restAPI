from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='home'),
    path('api/video', views.videoApi),
    path('api/video/<id>', views.videoApi, name='videoApi'),

    path('api/video-stat', views.videoStatApi),
    path('api/video-stat/<id>', views.videoStatApi, name='videoStatApi'),

]
