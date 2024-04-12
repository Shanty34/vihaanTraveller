from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home/index.html")


def second(request):
    return render(request, "home/second.html")
