

from dataclasses import field
from rest_framework.serializers import ModelSerializer
from medias.models import Media


class MediaSerializer(ModelSerializer):

    class Meta:
        model = Media
        fields = ['name']
