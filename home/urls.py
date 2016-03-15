from django.conf.urls import patterns, url
from home import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'proyecto_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',  views.index_view, name='index_view'),
    url(r'^login/',  views.login_view, name='login_view'),
    url(r'^logout/$',  views.logout_view, name='logout_view'),
    url(r'^formulario/$',  views.formulario_view, name='vista_formulario'),
    #url(r'^registro/$',  views.registro_view, name='registro_view'),
]
