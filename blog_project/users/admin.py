from django.contrib import admin

# Register your models here.
from .models import profile , user_model
admin.site.register(profile.Profile)
admin.site.register(user_model.User)
