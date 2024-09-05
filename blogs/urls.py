from django.urls import path
from blogs import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:id>/', views.get_blog, name='blog'),
    path('create/', views.create_blog, name='create_blog'),
    path('edit/', views.edit_blog, name='edit_blog')
]