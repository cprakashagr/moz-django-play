from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=25)
    phoneNumber = models.CharField(max_length=15)
    language = models.CharField(max_length=2)
    currency = models.CharField(max_length=3)


class Polygons(models.Model):
    area = models.TextField()
