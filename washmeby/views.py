# -*- coding: utf-8 -*-
from django.shortcuts import render
from wash.models import CarWash


def home(request):
    return render(request, "washmeby/index.html", { 'washes': CarWash.objects.all() })
    
