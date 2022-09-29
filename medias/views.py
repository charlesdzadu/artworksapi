import os
import requests
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import StreamingHttpResponse



from medias.models import Media
from medias.serializers import MediaSerializer




class MediasViewSet(ViewSet):
    serializer_class = MediaSerializer
    
    def get_queryset(self):
        medias = Media.objects.all()
        return medias

    @action(detail=False , methods=['get'])
    def disable(self, request):
        """ Cette fonction permet de désactiver les médias"""
        return  Response(data = "Je ne sais pas")
    
   

    


    

