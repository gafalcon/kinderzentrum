from django.shortcuts import render, render_to_response
#from registro.modelos.alimentacion_models import AlimentacionCostumbres
from cita.forms import * #Ficha_DatosForm, Ficha_TerapiaForm, Ficha_TerapistaForm
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator


class ReservarCitaView(View):
    template_name = 'cita/reservar_cita.html'

    def get(self, request, *args, **kwargs):
        paciente = Ficha_DatosForm(prefix="paciente")
        tipoTerapia = Ficha_TerapiaForm(prefix="tipoterapia")
        terapista = Ficha_TerapistaForm(prefix="terapista")

        return render(request, self.template_name,
              {'ficha_datos_form':paciente,
               'ficha_terapia_form':tipoTerapia,
               'ficha_terapista_form':terapista,
               'pagina_actual':'cita'}
        )


    def post(self, request, *args, **kwargs):
        paciente = Ficha_DatosForm(prefix="paciente")
        tipoTerapia = Ficha_TerapiaForm(prefix="tipoterapia")
        terapista = Ficha_TerapistaForm(prefix="terapista")

        if paciente.is_valid() and tipoTerapia.is_valid() and terapista.is_valid():
            paciente_data = paciente.cleaned_data
            tipoTerapia_data = tipoTerapia.cleaned_data
            terapista_data = terapista.cleaned_data

            print("datos is valid")
            print("datos", paciente_data)
            print("TipoTerapia", tipoTerapia_data)
            print("Terapista", terapista_data)

            # PacienteId = ...
            # cita = Cita()
            # cita.paciente_id = nombrePacienteinteger
            # cita.save()
            #...

            return render(request, self.template_name,
                      {'ficha_datos_form':paciente,
                       'ficha_terapia_form':tipoTerapia,
                       'ficha_terapista_form':terapista,
                       'pagina_actual':'cita'}
            )
            

        else:
            print("datos is invalid")
            print("\n\nErrors paciente:", paciente.errors)
            print("\n\nErrors TipoTerapia:", tipoTerapia.errors)
            print("\n\nErrors Terapista:", terapista.errors)
            
        return HttpResponseRedirect('/cita')
        