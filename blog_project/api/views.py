from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from api.serializers.blog_post import PostSerializer, UserSerializer
from blog.models.blog_post import Post


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpdatePost(generics.UpdateAPIView):
    pass


class DeletePost(generics.DestroyAPIView):
    pass


class CreatePost(generics.CreateAPIView):
    pass



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer