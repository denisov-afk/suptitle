from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import AbstractUser, PermissionsMixin

CHOICES = [('L', 'Left'), ('R', 'Right'), ('C', 'Center')]

CAPTIONS_STYLES = [
    ('standart_captions', 'Standart captions'),
    ('minimal_captions', 'Minimal captions'),
]

HEADLINE_STYLES = [
    ('standart_headline', 'Standart headline'),
    ('minimal_headline', 'Minimal headline'),
]

ASPECT_RATIOS = [
    ('widescreen', '16:9 Widescreen'),
    ('square', '1:1 Square'),
    ('portrait', '4:5 Portrait'),
    ('vertical', '9:16 Vertical'),
]


class WebsiteUser(AbstractUser):
    is_activated = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='user_photos/', blank=True)

    class Meta(AbstractUser.Meta):
        pass


class Video(models.Model):
    user = models.ForeignKey(WebsiteUser, models.CASCADE)
    url = models.URLField()
    language_code = models.CharField(max_length=20, default='en_us')
    filename = models.CharField(max_length=255)
    uploaded = models.DateTimeField(auto_created=True, auto_now_add=True)
    captions = JSONField(blank=True, null=True)
    caption_style = models.CharField(max_length=100, default='standart_captions', choices=CAPTIONS_STYLES)
    aspect_ratio = models.CharField(max_length=100, default='widescreen', choices=ASPECT_RATIOS)
    caption_position_v = models.IntegerField(default=0)
    caption_position_h = models.CharField(choices=CHOICES, max_length=1, default='C')
    headline = models.CharField(max_length=100, default='')
    headline_style = models.CharField(max_length=100, default='standart_headline', choices=HEADLINE_STYLES)
    headline_position_h = models.CharField(choices=CHOICES, max_length=1, default='C')
    headline_position_v = models.IntegerField(default=0)
    zoom = models.IntegerField(default=1)
    background_color = models.CharField(max_length=100, default='black')

    def __str__(self):
        return self.url
