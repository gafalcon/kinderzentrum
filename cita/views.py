from django.shortcuts import render, render_to_response
from cita.forms import Ficha_DatosForm
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .modelos.cita_model import Cita
#from django.utils.decorators import method_decorator


class ReservarCitaView(View):
    template_name = 'cita/reservar_cita.html'

    def get(self, request, *args, **kwargs):
        paciente = Ficha_DatosForm(prefix="paciente")
        context = {'ficha_datos_form':paciente, 'pagina_actual':'cita'}

        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        paciente = Ficha_DatosForm(prefix="paciente")
        context = {'ficha_datos_form':paciente, 'pagina_actual':'cita'}

        if paciente.is_valid():
            paciente_data = paciente.cleaned_data

            print("datos is valid")
            print("datos", paciente_data)
            return render(request, self.template_name, context)            

        else:
            print("datos is invalid")
            print("\n\nErrors paciente:", paciente.errors)            
            
        return HttpResponseRedirect('/cita')
        