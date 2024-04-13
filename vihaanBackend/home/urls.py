from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("second/", views.second, name="second"),
    path(
        "destinationDetails/<str:dest>",
        views.destinationDetails,
        name="destinationDetails",
    ),
    path(
        "itinerary/<int:page>",
        views.itinerary,
        name="itinerary",
    ),
]
