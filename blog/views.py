from django.shortcuts import render

from .models import Blogpost

def all_blogs(request):
    blogs = Blogpost.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

