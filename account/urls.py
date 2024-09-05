from django.urls import path
from account import views


urlpatterns = [
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('profile/', views.show_profile, name='profile'),
    path('logout/', views.logout_page, name='logout')
]