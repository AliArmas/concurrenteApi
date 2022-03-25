from django.db import models


class UserModel(models.Model):
    # id_user = models.TextField(primary_key=True)
    name = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    password = models.TextField(max_length=50)
