from rest_framework.decorators import api_view
from rest_framework.response import Response
from youtube.models import Video
from .serializers import VideoSerializers

from rest_framework import serializers
from rest_framework import status

@api_view(['GET'])
def all_videos(request):
  item = Video.objects.all()

  serializer = VideoSerializers(item, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def single_video(request, id):
  item = Video.objects.filter(pk = id).first()

  serializer = VideoSerializers(item, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)
