from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from . import fakemovies


hotels =   fakemovies.hotels



def index(request):
    title = "Etravel"
    return render(request, "hotels/index.html", {'hotels': hotels, 'title': title})