from django.contrib import admin

# Register your models here.
from modelos.medico_model import Medico
from modelos.paciente_model import Paciente
#from modelos.descripcion_models import Descripcion
from modelos.historial_madre_models import HistorialMadre, Gestacion
from modelos.nacimiento_models import Nacimiento
from modelos.familiars_models import Familiar


admin.site.register(Paciente)
admin.site.register(Familiar)
admin.site.register(Medico)
#admin.site.register(Descripcion)
admin.site.register(HistorialMadre)
admin.site.register(Gestacion)
