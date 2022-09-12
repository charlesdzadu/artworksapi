from django.db import models

class Media(models.Model):
    """La classe répresentant les médias """
    title = models.CharField(max_length=100) 
