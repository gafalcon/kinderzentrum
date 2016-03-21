from django.shortcuts import render, render_to_response
from registro.forms import * #Ficha_DatosForm, Ficha_DatosFamiliaresForm, Ficha_DatosMedicoForm, HistorialMadreForm
from django.template import RequestContext
from registro.modelos.familiars_models import DatosFamiliaresOtros
from registro.modelos.alimentacion_models import AlimentacionCostumbres
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


@method_decorator(login_required, name='dispatch')
class RegistroView(View):
    template_name = 'registro/registro_ficha_medica.html'

    def get(self, request, *args, **kwargs):
        datos = Ficha_PacienteForm(prefix="paciente")
        datos_familia = Ficha_DatosFamiliaresForm(prefix="familiares")
        datos_medico = Ficha_DatosMedicoForm(prefix="medico")
        historial_madre = Ficha_HistorialMadreForm(prefix="historial_madre")
        descripcion_paciente = Ficha_DescripcionPacienteForm(prefix="descripcion_paciente")
        recien_nacido = RecienNacidoForm(prefix="recien_nacido")
        primeros_dias = PrimerosDiasForm(prefix="primeros_dias")
        alimentacion = AlimentacionForm(prefix="alimentacion")
        suplementos_formset = SuplementosFormset(instance=AlimentacionCostumbres())
        datos_familiares = DatosFamiliaresOtrosForm(prefix="familiares_otros")
        hermanos_formset = HermanosFormset(instance=DatosFamiliaresOtros())
        return render(request, self.template_name,
                      {'ficha_datos_medico_form':datos_medico,
                       'ficha_datos_familia_form':datos_familia,
                       'ficha_datos_form':datos,
                       'descripcion_paciente':descripcion_paciente,
                       'historial_madre_form': historial_madre,
                       'recien_nacido': recien_nacido,
                       'alimentacion': alimentacion,
                       'suplementos_formset': suplementos_formset,
                       'datos_familiares': datos_familiares,
                       'hermanos_formset': hermanos_formset,
                       'primeros_dias': primeros_dias,
                       'pagina_actual':'registro'}
        )

    

    def post(self, request, *args, **kwargs):
        datos = Ficha_PacienteForm(request.POST, prefix="paciente")
        datos_familia = Ficha_DatosFamiliaresForm(request.POST, prefix="familiares")
        datos_medico = Ficha_DatosMedicoForm(request.POST, prefix="medico")
        historial_madre = Ficha_HistorialMadreForm(request.POST, prefix="historial_madre")
        descripcion_paciente = Ficha_DescripcionPacienteForm(request.POST, prefix="descripcion_paciente")
        recien_nacido = RecienNacidoForm(request.POST, prefix="recien_nacido")
        primeros_dias = PrimerosDiasForm(request.POST, prefix="primeros_dias")
        alimentacion = AlimentacionForm(request.POST, prefix="alimentacion")
        suplementos_formset = SuplementosFormset(request.POST, instance=AlimentacionCostumbres())
        datos_familiares = DatosFamiliaresOtrosForm(request.POST, prefix="familiares_otros")
        hermanos_formset = HermanosFormset(request.POST, instance=DatosFamiliaresOtros())

        if datos.is_valid() and datos_medico.is_valid() and datos_familia.is_valid() and recien_nacido.is_valid():
            print("datos is valid")
            print("Paciente", datos.cleaned_data)
            print("Medico", datos_medico.cleaned_data)
            print("Familiares", datos_familia.cleaned_data)
            print("Recien_nacido", recien_nacido.cleaned_data)
        else:
            print("datos is invalid")
            print("\n\nErrors paciente:", datos.errors)
            print("\n\nErrors medico:", datos_medico.errors)
            print("\n\nErrors familiares:", datos_familia.errors)
            print("\n\nErrors recien_nacido:", recien_nacido.errors)
            print("\n\nErrors primeros_dias:", primeros_dias.errors)
            print("\n\nErrors alimentacion:", alimentacion.errors)

            return render(request, self.template_name,
                          {'ficha_datos_form': datos,
                           'ficha_datos_familia_form': datos_familia,
                           'ficha_datos_medico_form': datos_medico,
                           'descripcion_paciente': descripcion_paciente,
                           'historial_madre_form': historial_madre,
                           'recien_nacido': recien_nacido,
                           'alimentacion': alimentacion,
                           'suplementos_formset': suplementos_formset,
                           'datos_familiares': datos_familiares,
                           'hermanos_formset': hermanos_formset,
                           'primeros_dias': primeros_dias,
                           'pagina_actual': 'registro'
                          })
        return HttpResponseRedirect('/')

       





# def registro_view(request):
#     if request.method == "POST":
#         datos = Ficha_PacienteForm(request.POST, prefix="paciente")
#         datos_medico = Ficha_DatosMedicoForm(request.POST, prefix="medico")
#         datos_familia = Ficha_DatosFamiliaresForm(request.POST, prefix="familiares")
#         primeros_dias = PrimerosDiasForm(request.POST, prefix="primeros_dias")
#         alimentacion = AlimentacionForm(request.POST, prefix="alimentacion")
#         recien_nacido = RecienNacidoForm(request.POST, prefix="recien_nacido")
#         if datos.is_valid() and datos_medico.is_valid() and datos_familia.is_valid() and recien_nacido.is_valid():
#             print("datos is valid")
#             print("Paciente", datos.cleaned_data)
#             print("Medico", datos_medico.cleaned_data)
#             print("Familiares", datos_familia.cleaned_data)
#             print("Recien_nacido", recien_nacido.cleaned_data)
#         else:
#             print("datos is invalid")
#             print("\n\nErrors paciente:", datos.errors)
#             print("\n\nErrors medico:", datos_medico.errors)
#             print("\n\nErrors familiares:", datos_familia.errors)
#             print(recien_nacido)
#             print("\n\nErrors recien_nacido:", recien_nacido.errors)
#             print("\n\nErrors primeros_dias:", primeros_dias.errors)
#             print("\n\nErrors alimentacion:", alimentacion.errors)

#             return render(request, 'registro/registro_ficha_medica.html',
#                           {'ficha_datos_form': datos,
#                            'ficha_datos_familia_form': datos_familia,
#                            'ficha_datos_medico_form': datos_medico,
#                            'recien_nacido': recien_nacido
#                           })
#         return HttpResponseRedirect('/')
#     datos = Ficha_PacienteForm(prefix="paciente")
#     print(datos)
#     datos_familia = Ficha_DatosFamiliaresForm(prefix="familiares")
#     datos_medico = Ficha_DatosMedicoForm(prefix="medico")
#     historial_madre = Ficha_HistorialMadreForm()
#     descripcion_paciente = Ficha_DescripcionPacienteForm()
#     recien_nacido = RecienNacidoForm(prefix="recien_nacido")
#     primeros_dias = PrimerosDiasForm(prefix="primeros_dias")
#     alimentacion = AlimentacionForm(prefix="alimentacion")
#     suplementos_formset = SuplementosFormset(instance=AlimentacionCostumbres())
#     datos_familiares = DatosFamiliaresOtrosForm()
#     hermanos_formset = HermanosFormset(instance=DatosFamiliaresOtros())
#     ctx = {'ficha_datos_medico_form':datos_medico,
#            'ficha_datos_familia_form':datos_familia,
#            'ficha_datos_form':datos,
#            'descripcion_paciente':descripcion_paciente,
#            'historial_madre_form': historial_madre,
#            'recien_nacido': recien_nacido,
#            'alimentacion': alimentacion,
#            'suplementos_formset': suplementos_formset,
#            'datos_familiares': datos_familiares,
#            'hermanos_formset': hermanos_formset,
#            'primeros_dias': primeros_dias,
#            'pagina_actual':'registro'}
#     return render(request, 'registro/registro_ficha_medica.html', ctx)

