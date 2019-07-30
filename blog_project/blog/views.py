from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.

# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    # <app>/<model>_<viewtype>.html
    # if we use this convention, we don't have to set template name
    template_name = 'blog/home.html'
    # if we access our variable using object we don't have to
    #change this
    context_object_name = 'posts'
    ordering = ['date_posted',]


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'





def about(request):
    return render(request, 'blog/about.html')
