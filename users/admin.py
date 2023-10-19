from django.contrib import admin

# Register your models here.

from .models import Profile, skill,Message

admin.site.register(Profile)
admin.site.register(skill)
admin.site.register(Message)