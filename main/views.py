from django.shortcuts import render

from main.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'main/index.html', {'posts': posts})