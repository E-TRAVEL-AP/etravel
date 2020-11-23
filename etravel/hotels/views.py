from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail 
from django.contrib.auth.models import User
import random

#######################################################################################################################################

def about(request):
    return render(request, 'about.html')

#######################################################################################################################################

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, help_text='Enter your first name')
    email = forms.EmailField(max_length=64, help_text='Enter a valid email address')
    

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('first_name', 'email',)


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            first_name = form.data.get('first_name')
            email = form.cleaned_data.get('email')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)

            subject = 'Travel with Us!!'
            message = f'Hi {first_name},\nThank you for registering on JARThreeDeeWale!! \nEnjoy shopping on our site!'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [email, ] 
            send_mail( subject, message, email_from, recipient_list ) 

            return redirect("/")

            

            
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            

    form = SignUpForm
    context = {'form': form}
    return render(request, "register.html", context)

#######################################################################################################################################

def logout_request(request):
    logout(request)
    return redirect("/")
    # messages.info(request, "logged out succesfully")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
        else:
                messages.error(request, "Invalid username or password")


    form = AuthenticationForm()
    context = {'form': form}
    return render(request, "login.html", context)

#######################################################################################################################################