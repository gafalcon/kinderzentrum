from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'kinderzentrum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^registro/', include('registro.urls')),
    url(r'^', include('home.urls')),
    url(r'^cita/', include('cita.urls')),
    url(r'^asistencia/', include('asistencia.urls')),
    url(r'^pagos/', include('pago.urls')),
]
