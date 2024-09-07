from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    print(request.user)
    return render(request, 'blogs/home.html')

# Get  blog details
def get_blog(request, id):
    try:
        blog_obj = Blog.objects.get(id = id)
    except Exception as e:
        print(e)
    return render(request, 'blogs/blog.html',{
        'blog' : blog_obj
    })


def create_blog(request):
    return render(request, 'blogs/create_blog.html')

def edit_blog(request):
    return render(request, 'blogs/create_blog.html',{
        'update' : "update"
    })