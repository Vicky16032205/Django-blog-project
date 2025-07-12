# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello World! , I am home")
    return render(request , 'home.html')

def aboutpage(request):
    # return HttpResponse("this is about page")
    return render(request , 'about.html')