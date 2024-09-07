from django.shortcuts import redirect, render
from .models import *
from .forms import  BlogForm

# Create your views here.

def home(request):
    return render(request, 'blogs/home.html',{
        'user' : request.user
    })

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
    category = Category.objects.all().order_by("category_name")
    if request.method == 'POST':
        frm = BlogForm(request.POST)
        category = request.POST.get('category')
        title = request.POST.get('title')
        banner = request.FILES.get('banner')

        if frm.is_valid():
            content = frm.cleaned_data['content']

            Blog.objects.create(
                title = title,
                content = content,
                category = Category.objects.get(id = category),
                user = request.user,
                image = banner
            )
            return redirect('/')

    return render(request, 'blogs/create_blog.html',{
        'frm': BlogForm,
        'categories' : category
    })


def edit_blog(request, id):
    return render(request, 'blogs/create_blog.html',{
        'update' : "update"
    })


def delete_blog(request, id):
    return redirect('/profile')