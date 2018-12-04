from django.shortcuts import render
from django.http import HttpResponse
from .models import Feedback

def index(request):
    return render(request,'feedback/index.html',{'Feedback':Feedback})
