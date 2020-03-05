from rest_framework.serializers import ModelSerializer

from website.models import Video


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['language_code',
                  'captions',
                  'url',
                  'user',
                  'filename',
                  'uploaded',
                  ]


class VideoCaptionsSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['captions']
