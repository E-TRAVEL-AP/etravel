from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register/', views.register, name="register"), 
    path('login/', views.login_request, name="login"), 
    path('logout/', views.logout_request, name="logout"),
    path('hotels/', views.hotels, name="hotels"),
    path('flights/', views.flights, name="flights"),
    path('test/', views.prediction, name="test"),
]