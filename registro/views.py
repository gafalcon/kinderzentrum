from django.shortcuts import render, render_to_response
from registro.forms import *
from django.template import RequestContext
from registro.modelos.paciente_model import Paciente
from registro.modelos.familiars_models import DatosFamiliaresOtros
from registro.modelos.alimentacion_models import AlimentacionCostumbres
from registro.modelos.recien_nacido_model import RecienNacido
from registro.modelos.medico_model import Medico
from registro.modelos.historial_madre_models import Actividad_Gestacion, Situacion_Gestacion
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.forms import formset_factory
# Create your views here.


@method_decorator(login_required, name="dispatch")
class RegistroView(View):
    template_name = 'registro/registro_ficha_medica.html'
    def get(self, request, *args, **kwargs):
        #datos = Ficha_PacienteForm(prefix="paciente")
        datos = PacienteForm(prefix="paciente")
        #datos_familia = Ficha_DatosFamiliaresForm(prefix="familiares")
        datos_familia = DatosFamiliaresFormset(data=data_formsets)
        #datos_medico = Ficha_DatosMedicoForm(prefix="medico")
        #datos_medico = DatosMedicoForm(prefix="medico")
        datos_medico = DatosMedicoFormset(data=data_formsets)
        historial_madre = Ficha_HistorialMadreForm(prefix="historial_madre")
        #descripcion_paciente = Ficha_DescripcionPacienteForm(prefix="descripcion_paciente")
        descripcion_paciente = DescripcionPacienteForm(prefix="descripcion_paciente")
        medicamento_formset = MedicamentoFormset(instance=Descripcion())
        gestacion = DesarrolloDeLaGestacionForm(prefix="gestacion")
        actividad_gestacion = ActividadGestacionFormset(initial=[{'nombre_actividad':x} for x in Actividad_Gestacion.ACTIVIDADES_CHOICES])
        situacion_gestacion = SituacionGestacionFormset(initial=[{'nombre_situacion':x} for x in Situacion_Gestacion.SITUACIONES_CHOICES])
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
                      {'datos_medico_formset':datos_medico,
                       'datos_familia_formset':datos_familia,
                       'ficha_datos_form':datos,
                       'descripcion_paciente':descripcion_paciente,
                       'medicamento_formset':medicamento_formset,
                       'historial_madre_form': historial_madre,
                       'gestacion': gestacion,
                       'actividad_gestacion':actividad_gestacion,
                       'situacion_gestacion':situacion_gestacion,
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
        datos_paciente = PacienteForm(request.POST, prefix="paciente")
        datos_familia = DatosFamiliaresForm(request.POST, prefix="familiares")
        datos_medico = DatosMedicoFormset(request.POST)
        #datos_medico = DatosMedicoForm(request.POST, prefix="medico")
        historial_madre = Ficha_HistorialMadreForm(request.POST, prefix="historial_madre")
        #descripcion_paciente = Ficha_DescripcionPacienteForm(request.POST, prefix="descripcion_paciente")
        descripcion_paciente = DescripcionPacienteForm(request.POST, prefix="descripcion_paciente")
        medicamento_formset = MedicamentoFormset(request.POST, instance=Descripcion())
        gestacion = DesarrolloDeLaGestacionForm(request.POST, prefix="gestacion")
        actividad_gestacion = ActividadGestacionFormset(request.POST)
        situacion_gestacion = SituacionGestacionFormset(request.POST)

        datos_nacimiento = NacimientoForm(request.POST, prefix="nacimiento")
        datos_recien_nacido = RecienNacidoForm(request.POST, prefix="recien_nacido")
        datos_primeros_dias = PrimerosDiasForm(request.POST, prefix="primeros_dias")
        datos_alimentacion = AlimentacionForm(request.POST, prefix="alimentacion")
        suplementos_formset = SuplementosFormset(request.POST, instance=AlimentacionCostumbres())
        datos_familiares = DatosFamiliaresOtrosForm(request.POST, prefix="familiares_otros")
        hermanos_formset = HermanosFormset(request.POST, instance=DatosFamiliaresOtros())

        if (datos_paciente.is_valid() and
            datos_medico.is_valid() and
            #datos_familia.is_valid() and
            # datos_nacimiento.is_valid() and
            #datos_recien_nacido.is_valid()): 
            datos_alimentacion.is_valid() and
            #datos_familiares.is_valid()):
            datos_primeros_dias.is_valid()):

            print("Paciente", datos_paciente.cleaned_data)
            paciente = self.create_paciente(datos_paciente.cleaned_data)
            print("Paciente", paciente)

            #recorremos cada uno de los forms de cada medico
            for form in datos_medico:
                print "Medico",form.cleaned_data
            #medico = self.create_medico(datos_medico.cleaned_data)
            #paciente.medico = medico
            # medico.save()

            # print("Familiar", datos_familia.cleaned_data)
            # familiar = self.create_familiar(datos_familia.cleaned_data)
            # print("Familiar", familiar)

            # nacimiento = datos_nacimiento.save()
            # paciente.nacimiento = nacimiento
            
            # recien_nacido = datos_recien_nacido.save(complicaciones_list=request.POST.getlist("recien_nacido-complicaciones_nacimiento"))
            # paciente.recien_nacido = recien_nacido

            print("Primeros dias", datos_primeros_dias.cleaned_data)
            primeros_dias = datos_primeros_dias.save()

            print("Alimentacion", datos_alimentacion.cleaned_data)
            alimentacion = datos_alimentacion.save()

            #print("FamiliaresOtros", datos_familiares.cleaned_data)
            #paciente.save()
            #familiar.paciente = paciente
            #familiar.save()
            return HttpResponseRedirect('/')
        else:
            print("datos is invalid")
            print("\n\nErrors paciente:", datos_paciente.errors)
            # print("\n\nErrors medico:", datos_medico.errors)
            # print("\n\nErrors familiares:", datos_familia.errors)
            # print("\n\nErrors nacimiento:", datos_nacimiento.errors)
            #print("\n\nErrors recien_nacido:", datos_recien_nacido.errors)
            print("\n\nErrors primeros_dias:", datos_primeros_dias.errors)
            #print("\n\nErrors alimentacion:", datos_alimentacion.errors)
            #print("Errors DatosFamiliares", datos_familiares.errors)
            return render(request, self.template_name,
                          {'ficha_datos_form': datos_paciente,
                           'datos_familia_formset': datos_familia,
                           'datos_medico_formset': datos_medico,
                           'descripcion_paciente': descripcion_paciente,
                           'medicamento_formset':medicamento_formset,
                           'historial_madre_form': historial_madre,
                           'gestacion': gestacion,
                           'actividad_gestacion':actividad_gestacion,
                           'situacion_gestacion':situacion_gestacion,
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

