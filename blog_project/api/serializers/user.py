
from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models.blog_post import Post


class UserSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'post']