from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.root, name = "localhost"),
    path('get/<str:audio_type>', views.get, name = 'get_audio_playlist'),
    path('get/<str:audio_type>/<int:audio_id>', views.get, name = 'get_audio_file'),
    path('update/<str:audio_type>/<int:audio_id>', views.update, name = "update_audio_file"),
    path('delete/<str:audio_type>/<int:audio_id>', views.delete, name = "delete_audio_file"),
    path('create/<str:audio_type>', views.create, name = "create_audio_file"),
]