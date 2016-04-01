from django.shortcuts import render, render_to_response
from registro.forms import * #Ficha_DatosForm, Ficha_DatosFamiliaresForm, Ficha_DatosMedicoForm, HistorialMadreForm
from django.template import RequestContext
from registro.modelos.paciente_model import Paciente
from registro.modelos.familiars_models import DatosFamiliaresOtros
from registro.modelos.alimentacion_models import AlimentacionCostumbres
from registro.modelos.recien_nacido_model import RecienNacido
from registro.modelos.medico_model import Medico
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
        nacimiento = NacimientoForm(prefix="nacimiento")
        datos_recien_nacido = RecienNacidoForm(prefix="recien_nacido",
                                               initial={'tiempo_apego_precoz': RecienNacido.APEGO_PRECOZ_NADA,
                                                        'tipo_contacto': RecienNacido.CONTACTO_NINGUNA})
        primeros_dias = PrimerosDiasForm(prefix="primeros_dias", initial={'icteria': False})
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
                       'nacimiento': nacimiento,
                       'recien_nacido': datos_recien_nacido,
                       'alimentacion': alimentacion,
                       'suplementos_formset': suplementos_formset,
                       'datos_familiares': datos_familiares,
                       'hermanos_formset': hermanos_formset,
                       'primeros_dias': primeros_dias,
                       'pagina_actual':'registro'}
        )

    def create_paciente(self, form_data):
        return Paciente(
            nombres = form_data['nombres'],
            apellidos = form_data['apellidos'],
            fecha_nacimiento = form_data['nacimiento'],
            nacionalidad = form_data['nacionalidad'],
            grupo_sanguineo = form_data['grupo_sanguineo'],
            sexo = form_data['sexo']
        )

    def create_familiar(self, form_data):
        return Familiar(
            nombres = form_data['nombres'],
            apellidos = form_data.get('apellidos'),
            parentesco = form_data.get('parentesco'),
            nivel_estudio = form_data.get('nivel_estudio'),
            direccion = form_data.get('direccion'),
            telefonos = form_data.get('telefono'),
            empresa = form_data.get('empresa'),
            direccion_empresa = form_data.get('direccion_empresa'),
            jornada = form_data.get('jornada')
        )

    def create_medico(self, form_data):
        return Medico(
            nombres = form_data['nombres'],
            apellidos = form_data['apellidos'],
            area = form_data['area'],
            direccion = form_data['direccion'],
            telefonos = form_data['telefono']
        )

    def post(self, request, *args, **kwargs):
        datos_paciente = Ficha_PacienteForm(request.POST, prefix="paciente")
        datos_familia = Ficha_DatosFamiliaresForm(request.POST, prefix="familiares")
        datos_medico = Ficha_DatosMedicoForm(request.POST, prefix="medico")
        historial_madre = Ficha_HistorialMadreForm(request.POST, prefix="historial_madre")
        descripcion_paciente = Ficha_DescripcionPacienteForm(request.POST, prefix="descripcion_paciente")
        datos_nacimiento = NacimientoForm(request.POST, prefix="nacimiento")
        datos_recien_nacido = RecienNacidoForm(request.POST, prefix="recien_nacido")
        datos_primeros_dias = PrimerosDiasForm(request.POST, prefix="primeros_dias")
        datos_alimentacion = AlimentacionForm(request.POST, prefix="alimentacion")
        suplementos_formset = SuplementosFormset(request.POST, instance=AlimentacionCostumbres())
        datos_familiares = DatosFamiliaresOtrosForm(request.POST, prefix="familiares_otros")
        hermanos_formset = HermanosFormset(request.POST, instance=DatosFamiliaresOtros())

        if (datos_paciente.is_valid() and
            # datos_medico.is_valid() and
            # datos_familia.is_valid() and
            # datos_nacimiento.is_valid() and
            # datos_recien_nacido.is_valid() and
            # datos_primeros_dias.is_valid() and
            datos_alimentacion.is_valid() and
            datos_familiares.is_valid()):

            num_hermanos = datos_familiares.cleaned_data.get('numero_hermanos', 0)
            print("Num hermanos", num_hermanos)
            suplementos = datos_alimentacion.cleaned_data.get('suplementos')
            print "\n\n\nSuplementos", suplementos

            if ((num_hermanos <= 0 or (num_hermanos > 0 and hermanos_formset.is_valid())) and
                    (not suplementos or (suplementos and suplementos_formset.is_valid()))):

                print("Paciente", datos_paciente.cleaned_data)
                paciente = self.create_paciente(datos_paciente.cleaned_data)
                print("num hermanos forms", len(hermanos_formset.forms))
                print("FamiliaresOtros", datos_familiares.cleaned_data)
                familiares = datos_familiares.save()
                paciente.datos_familiares = familiares


                if num_hermanos > 0:
                    for i in range(0, num_hermanos):
                        hermano = (hermanos_formset.forms[i]).save(commit=False)
                        hermano.datos_familiares = familiares
                        hermano.save()
            

                return HttpResponseRedirect('/')

            # medico = self.create_medico(datos_medico.cleaned_data)
            # paciente.medico = medico
            # medico.save()

            # print("Familiar", datos_familia.cleaned_data)
            # familiar = self.create_familiar(datos_familia.cleaned_data)
            
            # print("Nacimiento", datos_nacimiento.cleaned_data)
            # nacimiento = datos_nacimiento.save()
            # paciente.nacimiento = nacimiento
            
            # print("Recien Nacido", datos_recien_nacido.cleaned_data)
            # recien_nacido = datos_recien_nacido.save(complicaciones_list=request.POST.getlist("recien_nacido-complicaciones_nacimiento"))
            # paciente.recien_nacido = recien_nacido

            # print("Primeros dias", datos_primeros_dias.cleaned_data)
            # primeros_dias = datos_primeros_dias.save()
            # paciente.primeros_dias = primeros_dias

            # print("Alimentacion", datos_alimentacion.cleaned_data)
            # alimentacion = datos_alimentacion.save()
            # paciente.alimentacion = alimentacion

            

            #paciente.save()
            #familiar.paciente = paciente
            #familiar.save()
        print("datos is invalid")
        # print("\n\nErrors paciente:", datos_paciente.errors)
        # print("\n\nErrors medico:", datos_medico.errors)
        # print("\n\nErrors familiares:", datos_familia.errors)
        # print("\n\nErrors nacimiento:", datos_nacimiento.errors)
        # print("\n\nErrors recien_nacido:", datos_recien_nacido.errors)
        # print("\n\nErrors primeros_dias:", datos_primeros_dias.errors)
        # print("\n\nErrors alimentacion:", datos_alimentacion.errors)
        # print("Errors DatosFamiliares", datos_familiares.errors)
        print("Errors hermanos formset", hermanos_formset.errors)
        print "Errors suplementos formset", suplementos_formset.errors
        return render(request, self.template_name,
                      {'ficha_datos_form': datos_paciente,
                       'ficha_datos_familia_form': datos_familia,
                       'ficha_datos_medico_form': datos_medico,
                       'descripcion_paciente': descripcion_paciente,
                       'historial_madre_form': historial_madre,
                       'nacimiento': datos_nacimiento,
                       'recien_nacido': datos_recien_nacido,
                       'alimentacion': datos_alimentacion,
                       'suplementos_formset': suplementos_formset,
                       'datos_familiares': datos_familiares,
                       'hermanos_formset': hermanos_formset,
                       'primeros_dias': datos_primeros_dias,
                       'pagina_actual': 'registro'
                      })

       





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

