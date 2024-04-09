from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
  months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
  
  if month not in months:
    # return HttpResponse(f"<h1>Invalid month.</h1>")
    return HttpResponseNotFound("<h1>Invalid month.</h1>")
  else:
    return HttpResponse(f"<h1>You're on the {month} challenge.</h1>")