from django.contrib import admin

from bot.models import Message, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Message)
