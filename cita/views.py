from django.shortcuts import render, render_to_response
#from registro.modelos.alimentacion_models import AlimentacionCostumbres
from cita.forms import * #Ficha_DatosForm, Ficha_TerapiaForm, Ficha_TerapistaForm
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator

# Create your views here.
# def reservar_cita_view(request):
#     return render(request, 'cita/reservar_cita.html',{})
#

class ReservarCitaView(View):
    template_name = 'cita/reservar_cita.html'

    def get(self, request, *args, **kwargs):
        datos = Ficha_DatosForm(prefix="paciente")
        TipoTerapia = Ficha_TerapiaForm(prefix="tipoterapia")
        Terapista = Ficha_TerapistaForm(prefix="terapista")
        
        return render(request, self.template_name,
                      {'ficha_datos_form':datos,
                       'ficha_terapia_form':TipoTerapia,
                       'ficha_terapista_form':Terapista,
                       'pagina_actual':'cita'}
        )
