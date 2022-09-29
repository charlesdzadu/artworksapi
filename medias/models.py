from django.db import models

class Media(models.Model):
    """La classe répresentant les médias """
    
    name = models.CharField(max_length=100, help_text="Pour décrire un text") 