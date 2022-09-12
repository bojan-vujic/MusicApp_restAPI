from rest_framework import serializers
from youtube.models import Video, VideoStat


class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('__all__')


class VideoStatSerializers(serializers.ModelSerializer):
    class Meta:
        model = VideoStat
        fields = ('__all__')
