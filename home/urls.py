from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',  views.index_view, name='index_view'),
    )
