from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app_views/home.html')

def about(request):
    return render(request, 'app_views/about.html')