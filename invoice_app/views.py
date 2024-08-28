from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request, *args, **kwargs):
    return render(request, 'BASE.html')
