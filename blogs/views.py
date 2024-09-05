from django.shortcuts import render
from .models import *

# Create your views here.

# Get  blog details
def get_blog(request, id):
    try:
        blog_obj = Blog.objects.get(id = id)
    except Exception as e:
        print(e)
    return render(request, 'blog.html',{
        'blog' : blog_obj
    })