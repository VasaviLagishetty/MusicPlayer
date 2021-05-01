from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

# Create your models here.

class Songs(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded = models.DateTimeField(default = timezone.now)

class Podcasts(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded = models.DateTimeField(default = timezone.now)
    host = models.CharField(max_length=100)
    participants = ArrayField(
            models.CharField(max_length=100), size = 10, blank = True
          )

class AudioBook(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded = models.DateTimeField(default = timezone.now)