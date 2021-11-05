from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
  btitle = models.CharField(max_length=200)
  bauthor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
  btext = models.TextField()
  bcreated_date = models.DateTimeField(default = timezone.now)
  bpublished_date = models.DateTimeField(blank=True, null=True)
  def publish(self):
    self.published_date = timezone.now()
    self.save()
  def __str__(self):
    return self.btitle