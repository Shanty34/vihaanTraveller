from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home/index.html")


def second(request):
    return render(request, "home/second.html")


def destinationDetails(request, dest):
    return render(request, f"home/{dest}.html")


def itinerary(request, page):
    return render(request, f"home/itinerary_{page}.html")
