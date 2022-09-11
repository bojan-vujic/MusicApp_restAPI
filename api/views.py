from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from . serializers import VideoSerializers, VideoStatSerializers
from youtube.models import Video, VideoStat

@csrf_exempt
def videoApi(request, id=0):
  method = request.method.upper()

  if method == 'GET':
    videos = Video.objects.all()
    serializer = VideoSerializers(videos, many = True)
    return JsonResponse(serializer.data, json_dumps_params={'indent': 2}, safe = False)

  elif method == 'POST':
    data = JSONParser().parse(request)
    serializer = VideoSerializers(data = data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse('Video added.', safe = False)
    return JsonResponse('Something went wrong.')

  elif method == 'PUT':
    data = JSONParser().parse(request)
    video = Video.objects.get(pk = id)
    serializer = VideoSerializers(video, data = data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse('Video updated.', safe = False)
    return JsonResponse('Something went wrong.')


@csrf_exempt
def videoStatApi(request, id=0):
  method = request.method.upper()

  if method == 'GET':
    videos = VideoStat.objects.all()
    serializer = VideoStatSerializers(videos, many = True)
    return JsonResponse(serializer.data, json_dumps_params={'indent': 2}, safe = False)

  elif method == 'POST':
    data = JSONParser().parse(request)
    serializer = VideoStatSerializers(data = data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse('Video added.', safe = False)
    return JsonResponse('Something went wrong.')

  elif method == 'PUT':
    data = JSONParser().parse(request)
    video = VideoStat.objects.get(pk = id)
    serializer = VideoStatSerializers(video, data = data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse('Video updated.', safe = False)
    return JsonResponse('Something went wrong.')
