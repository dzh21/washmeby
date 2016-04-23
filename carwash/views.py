from django.shortcuts import render
# from django.views.generic import ListView
from .models import CarWash


def index(request):
    return render(request, "carwash/index.html", { 'carwashes': CarWash.objects.all() })
