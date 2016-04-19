# -*- coding: utf-8 -*-
from django.shortcuts import render
from carwash.models import CarWash


def home(request):
    return render(request, "washmeby/index.html", { 'carwashes': CarWash.objects.all() })
    
