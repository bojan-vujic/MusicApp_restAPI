from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from .models import Video, VideoStat, LastSearch
from .utils import *
from random import randrange
import os


def last_played():
  #print(datetime.now())
  #print(timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S"))
  #return timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
  return timezone.now()


YOUTUBE_API_KEYS = [
    'AIzaSyBKEJ-nq-mzZeKGnU87PID3UDHKnkZFPcQ',  # search videos 01
    'AIzaSyDUsdzLPDRljKXI4J3IurBqBHz14UqsEKw',  # search videos 02
    'AIzaSyCOf5mkRL41O4pBA7Q85ekHyGqwF-LGmjU',  # search videos 03
    'AIzaSyBCQhVH3WBLEPrPszRcsfTYgR1GknjxJOU',  # search videos 04
    'AIzaSyCFI6phHEEG2XmbHDPtwI_Ku1zr8qi6epI',  # search videos 05
    'AIzaSyDMitAmhMmqs_oc71U1ttZDni77D5R9xrE',  # search videos 06
]

def search(request):

  date_string = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")

  api_index   = randrange(len(YOUTUBE_API_KEYS))
  api_key     = YOUTUBE_API_KEYS[api_index]
  max_results = 25

  personal = [i.video_id for i in Video.objects.filter(personal=request.user).iterator()]

  if request.method == 'POST':
    search_string = request.POST.get('search')

    if len(search_string) > 0:
      searchResults = YouTubeSearch(search_string, api_key, max_results)

      # get list of videos (video_id from youtube)
      videos = searchResults['videos']

      totalResults = searchResults['totalResults']
      perPage = searchResults['perPage']

      # pass list of video id's to get all the additional for each video
      all_data = YouTubeVideos(videos, api_key)

      context = {
        'title' : 'Search results',
        'date_string': date_string,
        'search_string' : search_string,
        'totalResults' : totalResults,
        'perPage' : perPage,
        'videos_id': videos,
        'videos': all_data,
        'personal': personal,

        'api_key': api_key,
        'api_index': api_index + 1
      }

      if request.user.is_authenticated:
        item = LastSearch.objects.get_or_create(user=request.user)[0]

        item.user = request.user
        item.search = json.dumps(context, indent=2)
        item.date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S").date()
        item.save()

      return render(request, 'youtube/search.html', context)

    else:
      if request.user.is_authenticated:
        search = LastSearch.objects.filter(user=request.user).values()

        if not search.exists():
          return render(request, 'youtube/search.html', {'no_results' : True})

        else:
          json_data = search[0]['search'].replace("'", "\"")
          data = json.loads(json_data)
          context = data
          context['title'] = "Your previous search"
          context['personal'] = personal

          #print(json.dumps(context, indent=3))
          return render(request, 'youtube/search.html', context)

  return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def add_to_personal(request, video_id=None):
  video_id = str(video_id)
  info = video_data(request, video_id)

  item, created = Video.objects.get_or_create(video_id=video_id)

  # if item is created
  if created:
    item.title = info['title']
    item.duration = info['duration']
    item.save()
    item.personal.add(request.user)
    download_thumbnail(video_id)
  else:
    if not item.personal.filter(id=request.user.id).exists():
      item.personal.add(request.user)

  start = 0
  end   = info['duration']
  video = VideoStat(user=request.user, ytvideo=item, start=start, end=end)
  video.last_played = last_played()
  video.save()

  personal = [i.video_id for i in Video.objects.filter(personal=request.user).iterator()]
  search = LastSearch.objects.filter(user=request.user).values()
  json_data = search[0]['search'].replace("'", "\"")
  data = json.loads(json_data)
  context = data
  context['personal'] = personal

  return render(request, 'youtube/add_video.html', context)


def all_videos(request):
  videos = Video.objects.all()
  #for video in videos:
  #  download_thumbnail(video.video_id)
  context = {'videos' : videos}
  return render(request, 'youtube/all_videos.html', context)


@login_required
def history(request):
  videos = VideoStat.objects.filter(user=request.user) # apply sorting options
  video  = videos.first()
  hearted = [i.id for i in Video.objects.filter(favourites=request.user).iterator()]
  context = {
    'videos' : videos,
    'hearted' : hearted,
    'video': video,
    'total_videos': len(videos)
  }
  return render(request, 'youtube/history.html', context)


@login_required
def remove_video(request, video_id=None):
  video_id = str(video_id)

  video = Video.objects.get(video_id = video_id)

  if video.personal.filter(id=request.user.id).exists():
    video.personal.remove(request.user)

  if video.favourites.filter(id=request.user.id).exists():
    video.favourites.remove(request.user)

  #anonimus = User.objects.get(username = 'NullUser')
  vid = VideoStat.objects.get(ytvideo__video_id = video_id, user=request.user)
  #vid.user = anonimus
  #vid.save()
  vid.delete()

  videos = VideoStat.objects.filter(user=request.user)
  hearted = [i.id for i in VideoStat.objects.filter(ytvideo__favourites=request.user).iterator()]

  context = {'videos' : videos, 'hearted' : hearted}
  return render(request, 'youtube/history-partial.html', context)


@login_required
def heart_video(request, video_id=None):
  video_id = str(video_id)
  video = get_object_or_404(Video, video_id=video_id)
  if video.favourites.filter(id=request.user.id).exists():
    video.favourites.remove(request.user)
  else:
    video.favourites.add(request.user)

  videos = VideoStat.objects.filter(user=request.user)
  hearted = [i.id for i in Video.objects.filter(favourites=request.user).iterator()]

  context = {
    'videos' : videos,
    'hearted' : hearted,
    'total_videos': len(videos)}
  return render(request, 'youtube/history-partial.html', context)


def play_video(request, video_id = None):
  videos = VideoStat.objects.filter(user=request.user)
  video  = videos.filter(ytvideo__video_id=video_id).first()

  hearted = [i.id for i in Video.objects.filter(favourites=request.user).iterator()]

  context = {
    'videos' : videos,
    'hearted' : hearted,
    'video': video,
    'total_videos': len(videos)
  }

  return render(request, 'youtube/history.html', context)


def update_interval(request, video_id = None):
  if request.method == "POST":
    start = request.POST.get('start_val')
    end   = request.POST.get('end_val')

    video = VideoStat.objects.get(pk = video_id, user=request.user)
    video.start = start
    video.end = end
    video.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def update_counter(request, video_id = None):
  if request.method == "POST":
    video = VideoStat.objects.get(pk = video_id, user=request.user)
    video.repeats += 1
    video.last_played = last_played()
    video.replay_time += video.end - video.start
    video.save()
    video = VideoStat.objects.get(pk = video_id, user=request.user)

    context = {'video' : video}
    return render(request, 'youtube/history-video-iframe-info.html', context)



def show_info(request):

  return render(request, 'youtube/history-partial-info.html', {})
