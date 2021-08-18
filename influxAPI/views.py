from django.shortcuts import render
from .connector import *
from . models import Datas

# Create your views here.


def getData(request):
    if request.method == 'POST':
        data = request.POST['data']
        Datas.objects.create(data=data)
        # connectToInfluxDB(data)
        return render(request, 'influxAPI/home.html')

    else:
        return render(request, 'influxAPI/home.html')


def rawData(request, rdata):
    if request.method == 'POST':
        Datas.objects.create(data=rdata)
        return render(request, 'influxAPI/home.html')

    else:
        return render(request, 'influxAPI/home.html')
