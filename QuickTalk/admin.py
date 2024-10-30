from django.contrib import admin
from .models import *  # Import the custom Profile model

# Register the Profile model in the admin interface
admin.site.register(Profile)
admin.site.register(ChatRoom)
admin.site.register(Message)

# Register your models here.
