from django.shortcuts import render
from django.http import HttpResponse
from .models import Feedback,contact,subscription

def index(request):
    return render(request,'feedback/index.html',{'Feedback':Feedback})


def Contact(request):
    return render(request,'feedback/index.html',{'contact':contact})

def Subscription(request):
    return render(request,'feedback/index.html',{'sub': subscription})
