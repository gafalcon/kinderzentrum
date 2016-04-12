from django.conf.urls import patterns, url
from registro import views
from registro.views import *

urlpatterns =[ 
    # Examples:
    # url(r'^$', 'proyecto_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$',  views.registro_view, name='registro_view'),
    url(r'^$',  RegistroView.as_view(), name='registro_view'),
    url(r'busqueda_pacientes/', BusquedaPacientesView.as_view(), name='busqueda_pacientes'),
    url(r'pacientes/', PacienteListView.as_view(), name='pacientes-list')
    
]

