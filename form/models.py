from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, default=None)
    password = models.CharField(max_length=70, default=None)


