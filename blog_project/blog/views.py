from django.shortcuts import render
from .models import Post

# Create your views here.

posts = [{
    'date_posted': 'Monday ,may 16, 2019',
    'title': 'my first blog',
    'content': " Helo, I am new",
    'author': "John doe",
}
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
