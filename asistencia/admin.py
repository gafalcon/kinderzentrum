from django.contrib import admin
from asistencia.models import Bebe,Terapia,Cit,Tipo_terapia,Terapista,Terapia__Tipo_terapia

admin.site.register(Bebe)
admin.site.register(Terapia)
admin.site.register(Cit)

admin.site.register(Tipo_terapia)
admin.site.register(Terapista)
admin.site.register(Terapia__Tipo_terapia)
