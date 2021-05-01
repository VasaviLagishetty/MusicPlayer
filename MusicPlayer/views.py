from django.apps import apps
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Songs, Podcasts, AudioBook
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def create(request, audio_type, audio_id = ''):
    try:
        if request.method == "POST":
            json_data = json.loads(request.body)
            Model = apps.get_model('MusicPlayer', audio_type)
            Model.objects.create(**json_data)
            return HttpResponse("New Record Created")
        else:
            return HttpResponseBadRequest("Please check the request method, it should be POST method")
    except:
        return HttpResponseBadRequest("Please check input json format")

@csrf_exempt
def get(request, audio_type, audio_id = ''):
    if request.method == "GET":
        Model = apps.get_model('MusicPlayer', audio_type)
        if audio_id == '':
            playlist = Model.objects.filter()
            playlist = serializers.serialize('json', playlist)
        else:
            playlist = Model.objects.filter(id = audio_id)
            playlist = serializers.serialize('json', playlist)[1:-1]

        if len(playlist) == 0:
            return HttpResponse("No records found")
        return HttpResponse(playlist, content_type="text/json-comment-filtered")
    else:
        return HttpResponseBadRequest("Please check the request method, it should be GET method")

@csrf_exempt
def update(request, audio_type, audio_id = ''):
    try:
        if request.method == "PUT" or request.method == "POST":
            json_data = json.loads(request.body)
            Model = apps.get_model('MusicPlayer', audio_type)
            record = Model.objects.get(id = audio_id)
            for key, value in json_data.items():
                setattr(record, key, value)
                record.save(update_fields = [key])
            return HttpResponse("Audio file successfully updated")
        else:
            return HttpResponseBadRequest("Please check the request method, it should be either PUT or POST method")
    except:
        return HttpResponseBadRequest("Sorry, updation failed. Please check your input data and try again")
        
@csrf_exempt
def delete(request, audio_type, audio_id = ''):
    try:
        if request.method == "DELETE" or request.method == "POST":
            Model = apps.get_model('MusicPlayer', audio_type)
            Model.objects.get(id = audio_id).delete()
            return HttpResponse("Successfully Deleted")
        else:
            return HttpResponseBadRequest("Please check the request method, it should be either DELETE or POST method")
    except:
        return HttpResponseBadRequest("Sorry, deletion failed. No record found")

def root(request):
    return redirect("http://127.0.0.1:8000/admin")
