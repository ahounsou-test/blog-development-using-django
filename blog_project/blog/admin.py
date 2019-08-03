from django.contrib import admin

from .models.blog_post import Post

# Register your models here.

admin.site.register(Post)
