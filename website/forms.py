from django.forms.models import ModelForm
from .models import Video


class VideoUpdateForm(ModelForm):
    class Meta:
        model = Video
        exclude = ['url', 'filename', 'captions', 'uploaded', 'user', 'language_code']
