from django.urls import path
from . import views

urlpatterns = [
    path('<str:rdata>', views.getData, name='getdata'),
    path('rawdata/<str:rdata>', views.rawData, name='getrdata'),

]
