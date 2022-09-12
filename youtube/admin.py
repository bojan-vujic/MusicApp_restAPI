from django.contrib import admin
from .models import Video, VideoStat, LastSearch


class VideoAdmin(admin.ModelAdmin):
    list_display  = ('video_id', 'users_played_video', 'global_repeat', 'title', 'thumbnail', 'mmss', 'duration', 'id')
    search_fields = ['video_id',]

class LastSearchAdmin(admin.ModelAdmin):
    list_display  = ('user', 'date')
    search_fields = ['user',]

class VideoStatAdmin(admin.ModelAdmin):
    list_display  = ('username', 'videoId', 'title', 'last_played', 'replay_time', 'repeats', 'global_repeats', 'start', 'end', 'mmss', 'duration', 'id')
    #list_display  = ('global_repeats','videoId', 'title', 'last_played', 'replay_time', 'repeats', 'global_repeats', 'start', 'end', 'mmss', 'duration', 'id')
    search_fields = ['videoId',]

admin.site.register(Video, VideoAdmin)
admin.site.register(LastSearch, LastSearchAdmin)
admin.site.register(VideoStat, VideoStatAdmin)


#f5ygXQKF6M8
