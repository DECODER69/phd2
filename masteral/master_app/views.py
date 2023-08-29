from django.shortcuts import render
from django.shortcuts import render, redirect,  reverse

# Create your views here.
def pcg(request):
    return render(request, 'activities/index.html')

def list(request):
    return render (request, 'activities/breakdown.html')

def profile(request):
    return render(request, 'activities/profile.html')