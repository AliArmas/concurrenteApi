from django.db import models

# Create your models here.
class PhotoModel(models.Model):
    url = models.ImageField()