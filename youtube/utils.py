from django.conf import settings
import urllib.request
import json
import re
import os
from .models import LastSearch
import random
import string
from PIL import Image


def randStr(chars = string.ascii_uppercase + string.digits, N=10):
	return ''.join(random.choice(chars) for _ in range(N))

def seconds2min(s):
  a = str(s//3600)
  b = str((s%3600)//60)
  c = str((s%3600)%60)
  d = ["{}:{}".format(a*60 + b, c)]
  return d

# no key required youtube api with:
# https://yt.lemnoslife.com/

# https://www.youtube.com/watch?v=dGF1x14QNGA


def human_format(num):
  '''
  Converts number of views from INT into to k, M
  752000 -> 752k
  '''
  num = int(num)
  num = float('{:.3g}'.format(num))
  magnitude = 0
  while abs(num) >= 1000:
    magnitude += 1
    num /= 1000.0
  return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'k', 'M', 'B', 'T'][magnitude])


def YouTubeDuration(duration):
  '''
  Converts duration of a YouTube video from e.g. PT1H22M20S to hh:mm:ss
  '''
  match   = re.match('P((\d+)D)?T((\d+)H)?((\d+)M)?((\d+)S)?', duration).groups()
  days    = int(match[1]) if match[1] else 0
  hours   = int(match[3]) if match[3] else 0
  minutes = int(match[5]) if match[5] else 0
  seconds = int(match[7]) if match[7] else 0

  mins = (days * 24 + hours) * 60 + minutes
  secs = mins * 60 + seconds
  mmss = ":".join("%02d" % (i) for i in [mins, seconds])

  return {'YT' : duration, 'mmss' : mmss, 'seconds' : secs}


# First search for videos given string
def YouTubeSearch(search_string, api_key, max_results):
  base_url = 'https://www.googleapis.com/youtube/v3/search?'
  search_url = base_url \
      + 'part=id' \
      + '&q=' + search_string.replace(" ","+") \
      + '&key=' + api_key \
      + '&maxResults=' + str(max_results) \
      + '&type=video' \
      + 'order=relevance'
  response  = urllib.request.urlopen(search_url).read()
  data      = json.loads(response)
  #with open('json.json', 'w') as f:
  #  f.write("%s" % (json.dumps(data, indent=2)))

  #video_ids = [i['id']['videoId'] for i in data['items']]
  video_ids = []
  for i in data['items']:
    if i['id']['kind'] == 'youtube#video':
      video_ids.append(i['id']['videoId'])

  total     = data['pageInfo']['totalResults']
  perPage   = data['pageInfo']['resultsPerPage']

  return {'videos' : video_ids, 'totalResults': total, 'perPage' : perPage}


def YouTubeVideos(video_list, api_key):
  searchUrl = "https://www.googleapis.com/youtube/v3/videos?id=" \
              + ",".join([str(i) for i in video_list]) \
              + "&key=" \
              + api_key \
              + "&part=snippet,contentDetails,statistics&alt=json"
  print(searchUrl)
  response  = urllib.request.urlopen(searchUrl).read()
  data      = json.loads(response)

  output = []

  for i in data['items']:
    try:
      snippet   = i['snippet']
      title     = snippet['title']
      thumbnail = snippet['thumbnails']['medium']['url']

      cont      = i['contentDetails']
      duration  = cont['duration']

      stat      = i['statistics']
      viewCount = stat['viewCount']
      likeCount = stat['likeCount']
      commentCount = stat['commentCount']

      info = {
          'video_id'  : i['id'],
          'title'     : title.replace("'", "").replace('"', ''),
          'thumbnail' : thumbnail,
          'url'       : 'https://www.youtube.com/watch?v=' + i['id'],
          'duration'  : YouTubeDuration(duration),
          'viewCount' : human_format(viewCount),
          'likeCount' : human_format(likeCount),
          'commentCount' : human_format(commentCount)
      }
      output.append(info)
    except:
      pass

  return output


def video_data(request, video_id):
  # get the data from user's last search, that is where video info are stored
  # info will be used for adding the video to user's personal collection
  last_search = LastSearch.objects.filter(user=request.user).values()
  json_data = str(last_search[0]['search']).replace("'", "\"")
  data = json.loads(json_data)
  context = {}
  for i in data['videos']:
    if i['video_id'] == video_id:
      context = {
        'title' : i['title'],
        'duration' : i['duration']['seconds'],
      }
  return context


def display_time(seconds, granularity):
  intervals = (
      #('w', 604800),  # 60 * 60 * 24 * 7
      ('d',  86400),   # 60 * 60 * 24
      ('h',   3600),   # 60 * 60
      ('m',     60),
      ('s',      1),
  )
  result = []
  for name, count in intervals:
    value = seconds // count
    if value:
      seconds -= value * count
      if value == 1:
        name = name.rstrip('s')
      result.append("{:02d}{}".format(value, name))
    #else:
      #result.append("0{}".format( name))
  return ''.join(result[:granularity])


def download_thumbnail(video_id):
  url = "https://i.ytimg.com/vi/%s/mqdefault.jpg" % video_id
  thumbnail = os.path.join(settings.BASE_DIR, 'media', 'thumbnails', video_id + '.jpg')
  urllib.request.urlretrieve(url, thumbnail)

  img = Image.open(thumbnail)
  img = img.resize((170, 113), Image.ANTIALIAS)
  img.save(thumbnail)
  print(thumbnail)
