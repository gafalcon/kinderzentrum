from django.conf.urls import patterns, url
from pago import views

urlpatterns = [
    # Examples:
  url(r'^$', views.index_view, name='index_view'),
  url(r'^pacientes/(?P<patientId>)/$', views.patient_payments)
]
