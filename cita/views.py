from django.shortcuts import render, render_to_response
from cita.forms import* #Ficha_DatosForm, Ficha_ConsCitaTerapistaForm
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
        citapaciente = Ficha_DatosForm(prefix="citapaciente")
        cons_cita_terapista = Ficha_ConsCitaTerapistaForm(prefix="conscitaterapista")
        context = {'ficha_datos_form':citapaciente, 'ficha_cons_cita_terap_form':cons_cita_terapista,'pagina_actual':'cita'}

        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        citapaciente = Ficha_DatosForm(prefix="citapaciente")
        cons_cita_terapista = Ficha_ConsCitaTerapistaForm(prefix="conscitaterapista")
        context = {'ficha_datos_form':citapaciente, 'ficha_cons_cita_terap_form':cons_cita_terapista,'pagina_actual':'cita'}

        if citapaciente.is_valid() and cons_cita_terapista.is_valid():

            print("citapaciente is valid")
            print("cons_cita_terapista is valid")
            #print("datos", paciente_data)
            #paciente_data = paciente.cleaned_data
            #paciente_data.save()          
            #nombre_paciente = paciente.cleaned_data.get("Paciente")
            #paciente.save()
            #context = {'Mensaje': "La cita de %s se ha guardado exitosamente." $(nombre_paciente)}           

            return render(request, self.template_name, context)            

        else:
            print("citapaciente is invalid")
            print("\n\nErrors citapaciente:", citapaciente.errors)
            print("cons_cita_terapista is invalid")         
            print("\n\nErrors cons_cita_terapista:", cons_cita_terapista.errors) 
            
        return HttpResponseRedirect('/cita')
        