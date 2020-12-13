from django.shortcuts import render
from django.http      import HttpResponse
import datetime

# Create your views here.


# Create your views here

def hello(request):
    return HttpResponse('<h1>Hello world from Django my_app!! AAT.</h1>')

def get_date_time(request):
    dt = datetime.datetime.now()
    s = '<b>Current Date and Time: </b>' + str(dt)
    return HttpResponse(s)

