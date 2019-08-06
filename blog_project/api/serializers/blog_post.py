from rest_framework import serializers

from blog.models.blog_post import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'date_posted', 'author',]