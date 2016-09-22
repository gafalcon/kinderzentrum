from django.conf.urls import patterns, url
from cita.views import ReservarCitaView
from .views import *

urlpatterns =[ 
    
    url(r'^$',  ReservarCitaView.as_view(), name='reservar_cita_view'),
    
    
]