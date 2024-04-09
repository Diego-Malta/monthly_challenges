from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
 return HttpResponse("<h1>Hello, world. You're at the challenges for January.</h1>")

def february(request):
 return HttpResponse("<h1>You're on the February challenge.</h1>")