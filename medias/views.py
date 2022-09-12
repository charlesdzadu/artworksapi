from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


from medias.models import Media
from medias.serializers import MediaSerializer



class MediasViewSet(ModelViewSet):
    serializer_class = MediaSerializer
    def get_queryset(self):
        medias = Media.objects.all()
        return medias

    @action(detail=False, methods=['post'])
    def disable(self):
        """ Cette fonction permet de désactiver les médias"""
        return  Response()


    

