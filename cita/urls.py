from django.conf.urls import patterns, url
from cita.views import ReservarCitaView

urlpatterns =[ 
    
    url(r'^$',  ReservarCitaView.as_view(), name='reservar_cita_view'),
    
]