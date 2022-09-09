from rest_framework import serializers
from youtube.models import Video


class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('__all__')
