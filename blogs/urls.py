from django.urls import path
from blogs import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:id>/', views.get_blog, name='blog')
]