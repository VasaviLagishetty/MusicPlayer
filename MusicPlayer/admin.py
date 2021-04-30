from django.contrib import admin
from .models import Songs, Podcasts, AudioBook

# Register your models here.

admin.site.register(Songs)
admin.site.register(Podcasts)
admin.site.register(AudioBook)