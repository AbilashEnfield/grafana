from django.db import models



class Datas(models.Model):
    header      = models.TextField(null=True, blank=True)
    customer_id = models.TextField(null=True, blank=True)
    imei_number = models.TextField(null=True, blank=True)
    time        = models.DateTimeField(null=True, blank=True)
    di1         = models.TextField(null=True, blank=True)
    di2         = models.TextField(null=True, blank=True)
    di3         = models.TextField(null=True, blank=True)
    di4         = models.TextField(null=True, blank=True)
    do1         = models.TextField(null=True, blank=True)
    do2         = models.TextField(null=True, blank=True)
    do3         = models.TextField(null=True, blank=True)
    do4         = models.TextField(null=True, blank=True)
    ai1         = models.TextField(null=True, blank=True)
    ai2         = models.TextField(null=True, blank=True)
    ai3         = models.TextField(null=True, blank=True)
    ai4         = models.TextField(null=True, blank=True)
    modbus1     = models.TextField(null=True, blank=True)
    modbus2     = models.TextField(null=True, blank=True)
    modbus3     = models.TextField(null=True, blank=True)
    mcc         = models.TextField(null=True, blank=True)
    mnc         = models.TextField(null=True, blank=True)
    cell_id     = models.TextField(null=True, blank=True)
    ver         = models.TextField(null=True, blank=True)
    bat         = models.TextField(null=True, blank=True)
    pwrsts      = models.TextField(null=True, blank=True)
    gsmver      = models.TextField(null=True, blank=True)
    gsmsig      = models.TextField(null=True, blank=True)
    end         = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.customer_id)
