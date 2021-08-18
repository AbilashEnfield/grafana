from django.shortcuts import render
from .connector import *

# Create your views here.


def getData(request):
    if request.method == 'POST':
        data = request.POST['data']
        connectToInfluxDB(data)
        return render(request, 'influxAPI/home.html')

    else:
        return render(request, 'influxAPI/home.html')
