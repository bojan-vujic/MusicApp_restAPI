from django.urls import path
from . import views

urlpatterns = [
  path('search-results/', views.search, name="search-results"),
  path('music/<video_id>/add-personal/', views.add_to_personal, name="add_to_personal"),
  path('music/<video_id>/rem-personal/', views.remove_video, name="remove_video"),
  path('music/<video_id>/add-favorites/', views.heart_video, name="heart_video"),
  path('music/<video_id>/update_interval/', views.update_interval, name="update_interval"),
  path('music/<video_id>/update_counter/', views.update_counter, name="update_counter"),
  path('all_videos/', views.all_videos, name="all_videos"),
  path('my_music/', views.history, name="history"),
  path('my_music/play/<video_id>/', views.play_video, name="play_video"),
]


