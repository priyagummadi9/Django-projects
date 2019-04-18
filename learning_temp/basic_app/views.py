from django.shortcuts import render

def index(request):
    return render(request,'basic_app/index.html')

def other(request):
    return render(request,'basic_app/other.html')

def base(request):
    return render(request,'basic_app/base.html')

def url_temp(request):
    return render(request,'basic_app/url_temp.html')

# Create your views here.
