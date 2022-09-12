from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


from medias.models import Media



class MediasViewSet(ModelViewSet):

    def get_queryset(self):
        medias = Media.objects.all()
        return medias

