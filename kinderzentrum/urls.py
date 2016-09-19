from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
import home
import cita

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
    #url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset', name='reset_password_reset1'),
    url(r'^reset/password_reset/$', auth_views.password_reset, name='reset_password_reset1'),
    url(r'^reset/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^change/password/$', home.views.change_password, name='changepassword'),

    url(r'^get_citas/$', cita.views.get_citas, name='get_citas'),
    url(r'^get_cita/$', cita.views.get_cita, name='get_cita'),
    url(r'^save_cita/$', cita.views.save_cita, name='save_cita'),
    url(r'^delete_cita/$', cita.views.delete_cita, name='delete_cita'),
    url(r'^update_cita/$', cita.views.update_cita, name='update_cita'),

]
