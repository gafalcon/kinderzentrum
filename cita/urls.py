from django.conf.urls import patterns, url
from cita import views
from cita.views import ReservarCitaView

urlpatterns =[ 
    # Examples:
    # url(r'^$', 'proyecto_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$',  views.registro_view, name='registro_view'),
    url(r'^$',  ReservarCitaView.as_view(), name='reservar_cita_view'),
]

