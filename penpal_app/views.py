from django.shortcuts import render, redirect
from django.contrib import messages
import json
from datetime import datetime

def index(request):
    return render(request,'index.html')