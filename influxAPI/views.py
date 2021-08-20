from django.shortcuts import render
from .connector import *
from .slicer import data_slicer
from .models import Datas


# Create your views here.

def getData(request, rdata):
    processed_data = data_slicer(rdata)

    Datas.objects.create(
        header=processed_data["vii-pxpy-uqaheader"],
        customer_id=processed_data["id"],
        imei_number=processed_data["imei"],
        time=processed_data["time"],
        di1=processed_data["di1"],
        di2=processed_data["di2"],
        di3=processed_data["di3"],
        di4=processed_data["di4"],
        do1=processed_data["do1"],
        do2=processed_data["do2"],
        do3=processed_data["do3"],
        do4=processed_data["di4"],
        ai1=processed_data["ai1"],
        ai2=processed_data["ai2"],
        ai3=processed_data["ai3"],
        ai4=processed_data["ai4"],
        modbus1=processed_data["modbus1"],
        modbus2=processed_data["modbus2"],
        modbus3=processed_data["modbus3"],
        mcc=processed_data["mcc"],
        mnc=processed_data["mnc"],
        cell_id=processed_data["cellid"],
        ver=processed_data["ver"],
        bat=processed_data["bat"],
        pwrsts=processed_data["pwrsts"],
        gsmver=processed_data["gsmver"],
        gsmsig=processed_data["gsmsig"],
        end=processed_data["end"]
    )
    return render(request, 'influxAPI/home.html')


def rawData(request, rdata):
    processed_data = data_slicer(rdata)
    Datas.objects.create(
        header=processed_data["vii-pxpy-uqaheader"],
        customer_id=processed_data["id"],
        imei_number=processed_data["imei"],
        time=processed_data["time"],
        di1=processed_data["di1"],
        di2=processed_data["di2"],
        di3=processed_data["di3"],
        di4=processed_data["di4"],
        do1=processed_data["do1"],
        do2=processed_data["do2"],
        do3=processed_data["do3"],
        do4=processed_data["di4"],
        ai1=processed_data["ai1"],
        ai2=processed_data["ai2"],
        ai3=processed_data["ai3"],
        ai4=processed_data["ai4"],
        modbus1=processed_data["modbus1"],
        modbus2=processed_data["modbus2"],
        modbus3=processed_data["modbus3"],
        mcc=processed_data["mcc"],
        mnc=processed_data["mnc"],
        cell_id=processed_data["cellid"],
        ver=processed_data["ver"],
        bat=processed_data["bat"],
        pwrsts=processed_data["pwrsts"],
        gsmver=processed_data["gsmver"],
        gsmsig=processed_data["gsmsig"],
        end=processed_data["end"]
    )
    return render(request, 'influxAPI/home.html')
