from django.db import models
from django.utils import timezone

# Create your models here.
class Update(models.Model):
  item = models.TextField()
  date_added = models.DateTimeField(default = timezone.now)
  
  # by default it will order by an Id, we will change it to order
  # by desending order which means newest posts are showed first.
  class Meta:
    ordering = ['-date_added']
  
  def __str__(self):
    return self.item