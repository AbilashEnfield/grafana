from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData, name='getdata'),
    path('rawdata/<str:rdata>', views.rawData, name='getdata'),

]
