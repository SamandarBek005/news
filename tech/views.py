from django.http import request
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, "index.html")
def contact (request):
    return render(request, "contact.html")
def ttt (request):
    return render(request, "404.html")
