from django.shortcuts import render, redirect
from django.contrib import messages
import json
from datetime import datetime

def index(request):

    return render(request,'index.html')

def notfound(request):
    return render(request,'404.html')

def editprofile(request):
    return render(request,'edit-profile.html')

def chat(request):
    return render(request,'chat.html')

def faq(request):
    return render(request,'faq.html')

def profile(request):
    return render(request,'profile.html')

def tags(request):
    return render(request,'tags.html')

def contact(request):
    return render(request,'contact.html')
