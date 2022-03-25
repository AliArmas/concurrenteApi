from django.db import models

# Create your models here.
class PhotoModel(models.Model):
    image = models.ImageField()