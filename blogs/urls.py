from django.urls import path
from blogs import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:id>/', views.get_blog, name='blog'),
    path('create/', views.create_blog, name='create_blog'),
    path('edit/<int:id>', views.edit_blog, name='edit_blog'),
    path('elete/<int:id>', views.delete_blog, name='delete_blog')
]