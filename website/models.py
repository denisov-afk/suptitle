from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import AbstractUser, PermissionsMixin

CHOICES = [('L', 'Left'), ('R', 'Right'), ('C', 'Center')]


class WebsiteUser(AbstractUser):
    is_activated = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='user_photos/', blank=True)

    class Meta(AbstractUser.Meta):
        pass


class Video(models.Model):
    user = models.ForeignKey(WebsiteUser, models.CASCADE)
    url = models.URLField()
    filename = models.CharField(max_length=255)
    uploaded = models.DateTimeField(auto_created=True, auto_now_add=True)
    captions = JSONField(blank=True, null=True)
    caption_style = models.CharField(max_length=100, default='on process')
    aspect_ratio = models.CharField(max_length=100, default='on process')
    caption_position_v = models.IntegerField(default=0)
    caption_position_h = models.CharField(choices=CHOICES, max_length=1, default='C')
    headline = models.CharField(max_length=100, default='Headline')
    headline_style = models.CharField(max_length=100, default='on process')
    headline_position_h = models.CharField(choices=CHOICES, max_length=1, default='C')
    headline_position_v = models.IntegerField(default=0)
    zoom = models.IntegerField(default=1)
    background_color = models.CharField(max_length=100, default='on process')

    def __str__(self):
        return self.url
