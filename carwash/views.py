from django.shortcuts import render
from django.views.generic import ListView
from .models import CarWash


# Create your views here.
class CarWashList(ListView):
    model = CarWash
    