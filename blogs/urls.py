from django.urls import path
from blogs import views


urlpatterns = [
    path('blog/<int:id>/', views.get_blog, name='blog')
]