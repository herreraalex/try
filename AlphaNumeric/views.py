from django.shortcuts import render
import requests
from AlphaNumeric import templates
# Create your views here.

def index(request):
    context={'camilo':2}
    return render(request, "index/index.html",{'moreno':context})
