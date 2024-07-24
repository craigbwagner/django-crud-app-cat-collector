from django.shortcuts import render

# import HttpResponse to send text-based responses
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")
