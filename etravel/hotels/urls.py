from django.urls import path

from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('register/', views.register, name="register"), 
    path('login/', views.login_request, name="login"), 
    path('logout/', views.logout_request, name="logout"),
]