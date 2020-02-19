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
    uploaded = models.DateTimeField(auto_created=True)
    captions = JSONField(blank=True, null=False)
    caption_style = models.CharField(max_length=100)
    aspect_ratio = models.CharField(max_length=100)
    caption_position_v = models.IntegerField()
    caption_position_h = models.CharField(choices=CHOICES, max_length=1)
    headline = models.CharField(max_length=100)
    headline_style = models.CharField(max_length=100)
    headline_position_h = models.CharField(choices=CHOICES, max_length=1)
    headline_position_v = models.IntegerField()
    zoom = models.IntegerField()
    background_color = models.CharField(max_length=100)

    def __str__(self):
        return self.url
