from django.contrib import admin

# Register your models here.
from .models import Medico, Paciente
from .descripcion_models import Descripcion
from .historial_madre_models import HistorialMadre, Gestacion
from .nacimiento_models import Nacimiento
from .familiars_models import Familiar


admin.site.register(Paciente)
admin.site.register(Familiar)
admin.site.register(Medico)
admin.site.register(Descripcion)
admin.site.register(HistorialMadre)
admin.site.register(Gestacion)
