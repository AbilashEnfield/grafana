from django.shortcuts import render
from .connector import *
from . models import Datas

# Create your views here.


def getData(request, rdata):
    Datas.objects.create(data=rdata)
    return render(request, 'influxAPI/home.html')


def rawData(request, rdata):
    Datas.objects.create(data=rdata)
    return render(request, 'influxAPI/home.html')

