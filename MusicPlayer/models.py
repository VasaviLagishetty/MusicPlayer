from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

# Create your models here.

class Songs(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    name = models.CharField(max_length=100, blank=False)
    duration = models.PositiveIntegerField(blank=False)
    uploaded = models.DateTimeField(default = timezone.now)

class Podcasts(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    name = models.CharField(max_length=100, blank=False)
    duration = models.PositiveIntegerField(blank=False)
    uploaded = models.DateTimeField(default = timezone.now)
    host = models.CharField(max_length=100,blank=False)
    participants = ArrayField(
            models.CharField(max_length=100), size = 10, blank = True, default = list
          )

class AudioBook(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    title = models.CharField(max_length=100,blank=False)
    author = models.CharField(max_length=100, blank=False)
    narrator = models.CharField(max_length=100, blank=False)
    duration = models.PositiveIntegerField(blank=False)
    uploaded = models.DateTimeField(default = timezone.now)