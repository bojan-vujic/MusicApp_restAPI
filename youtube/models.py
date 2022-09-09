from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from time import gmtime
from time import strftime
from django.utils import timezone, dateformat


class LastSearch(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  search = models.TextField()
  date = models.DateField(default=None, blank=True, null=True)
  
  def __str__(self):
    return str(self.user.username)
  
  class Meta:
    verbose_name_plural = 'Last Search'
    #ordering = ['-date']

from .utils import display_time

class Video(models.Model):
  video_id   = models.CharField(max_length=30)
  title      = models.TextField(default=None, blank=True, null=True)
  duration   = models.IntegerField(default=None, blank=True, null=True)
  favourites = models.ManyToManyField(User, related_name='favourites', default=None, blank=True)
  personal   = models.ManyToManyField(User, related_name='personal', default=None, blank=True)
  
  @property
  def users_played_video(self):
    total = len(self.videostat_set.all())
    return total
  
  @property
  def global_repeat(self):
    items = self.videostat_set.filter(ytvideo_id = self.id)
    total = sum([i.repeats for i in items])
    return total

  @property
  def global_replay(self):
    items = self.videostat_set.filter(ytvideo_id = self.id)
    total = sum([i.replay_time for i in items])
    return total
  
  @property
  def users_hearted_video(self):
    return len(self.favourites)
  
  @property
  def mmss(self):
    t = int(self.duration)
    h = t // 3600
    m = t % 3600 // 60 + h * 60
    s = t % 3600 % 60
    return '{:02d}:{:02d}'.format(m, s)
  
  @property
  def url(self):
    return "https://www.youtube.com/watch?v=%s" % str(self.video_id)
  
  @property
  def thumbnail(self):
    #return "https://i.ytimg.com/vi/%s/default.jpg" % str(self.video_id)
    #return "https://i.ytimg.com/vi/%s/mqdefault.jpg" % str(self.video_id)
    return "/media/thumbnails/%s.jpg" % str(self.video_id)
    
  def __str__(self):
    return self.video_id


class VideoStat(models.Model):
  user    = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True, blank=True)
  ytvideo = models.ForeignKey(Video, on_delete=models.CASCADE)
  start   = models.IntegerField(blank=True, null=True)  # start (seconds) for video repeat
  end     = models.IntegerField(blank=True, null=True)  # end   (seconds)
  repeats = models.IntegerField(default=0, blank=True, null=True)  # number of repeats
  last_played = models.DateTimeField(default = timezone.now)
  replay_time = models.IntegerField(default=0, blank=True, null=True)

  @property
  def username(self):
    return str(self.user.username)
  
  @property
  def title(self):
    return self.ytvideo.title
  
  @property
  def duration(self):
    return self.ytvideo.duration
  
  @property
  def mmss(self):
    return self.ytvideo.mmss
  
  @property
  def url(self):
    return self.ytvideo.url
  
  @property
  def thumbnail(self):
    return self.ytvideo.thumbnail
  
  @property
  def videoId(self):
    return str(self.ytvideo.video_id)
  
  @property
  def users_played(self):
    return self.ytvideo.users_played_video

  @property
  def personal(self):
    return self.ytvideo.personal

  @property
  def global_repeats(self):
    return self.ytvideo.global_repeat
  
  @property
  def global_replays(self):
    return display_time(int(self.ytvideo.global_replay), 3)
  
  @property
  def your_replays(self):
    return display_time(int(self.replay_time), 3)
  
  @property
  def startmmss(self):
    t = strftime("%M %S", gmtime(self.start)).split()
    return "%i:%s" % (int(t[0]), t[1])

  @property
  def endmmss(self):
    t = int(self.end)
    h = t // 3600
    m = t % 3600 // 60
    s = t % 3600 % 60
    if h > 0:
      return '{:d}:{:02d}:{:02d}'.format(h, m, s)
    else:
      return '{:02d}:{:02d}'.format(m, s)

  @property
  def offsetleft(self):
    return str((self.start / self.duration) * 100)
  
  @property
  def offsetright(self):
    return str((self.end / self.duration) * 100)
  
  @property
  def last_time_played(self):
    formatted_date = dateformat.format(self.last_played, 'Y-m-d H:i')
    return formatted_date
  
  def __str__(self):
    return str(self.ytvideo.video_id)


