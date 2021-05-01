from django.apps import apps
from django.core import serializers
from django.core.exceptions import BadRequest
from django.shortcuts import render
from django.http import HttpResponse
from .models import Songs, Podcasts, AudioBook
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def get(request, audio_type, audio_id = ''):
    if request.method == "GET":
        Model = apps.get_model('MusicPlayer', audio_type)
        if audio_id == '':
            playlist = Model.objects.filter()
        else:
            playlist = Model.objects.filter(id = audio_id)

        if len(playlist) == 0:
            raise BadRequest

        playlist = serializers.serialize('json', playlist)
        return HttpResponse(playlist, content_type="text/json-comment-filtered")
        
@csrf_exempt
def delete(request, audio_type, audio_id = ''):
    if request.method == "DELETE":
        Model = apps.get_model('MusicPlayer', audio_type)
        Model.objects.get(id = audio_id).delete()
        return HttpResponse("Successfully Deleted")

@csrf_exempt
def update(request, audio_type, audio_id = ''):
    if request.method == "POST":
        json_data = json.loads(request.body)
        Model = apps.get_model('MusicPlayer', audio_type)
        record = Model.objects.get(id = audio_id)
        for key, value in json_data.items():
            setattr(record, key, value)
            record.save(update_fields = [key])
    return HttpResponse(record.host)

@csrf_exempt
def create(request, audio_type, audio_id = ''):
    if request.method == "POST":
        json_data = json.loads(request.body)
        Model = apps.get_model('MusicPlayer', audio_type)
        Model.objects.create(**json_data)
        return HttpResponse("New Record Created")

