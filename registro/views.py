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
        datos = PacienteForm(prefix="paciente")
        datos_familia = DatosFamiliaresFormset(prefix="familiares")
        datos_medico = DatosMedicoFormset(prefix="medico")

        historial_madre = HistorialMadreForm(prefix="historial_madre")
        descripcion_paciente = DescripcionPacienteForm(prefix="descripcion_paciente")
        medicamento_formset = MedicamentoFormset(instance=Descripcion())
        gestacion = DesarrolloDeLaGestacionForm(prefix="gestacion")
        actividad_gestacion = ActividadGestacionFormset(prefix="actividad",
                                                        initial=[{'nombre_actividad':x} for x in Actividad_Gestacion.ACTIVIDADES_CHOICES])
        situacion_gestacion = SituacionGestacionFormset(prefix="situacion",
                                                        initial=[{'nombre_situacion':x} for x in Situacion_Gestacion.SITUACIONES_CHOICES])
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
                       'pagina_actual':'registro'})

    def post(self, request, *args, **kwargs):
        datos_paciente = PacienteForm(request.POST, prefix="paciente")
        datos_familia = DatosFamiliaresFormset(request.POST, prefix="familiares")
        datos_medico = DatosMedicoFormset(request.POST, prefix="medico")
        datos_historial_madre = HistorialMadreForm(request.POST, prefix="historial_madre")
        datos_descripcion_paciente = DescripcionPacienteForm(request.POST, prefix="descripcion_paciente")
        medicamento_formset = MedicamentoFormset(request.POST, instance=Descripcion())
        datos_gestacion = DesarrolloDeLaGestacionForm(request.POST, prefix="gestacion")
        actividad_gestacion = ActividadGestacionFormset(request.POST, prefix="actividad")
        situacion_gestacion = SituacionGestacionFormset(request.POST, prefix="situacion")

        datos_nacimiento = NacimientoForm(request.POST, prefix="nacimiento")
        datos_recien_nacido = RecienNacidoForm(request.POST, prefix="recien_nacido")
        datos_primeros_dias = PrimerosDiasForm(request.POST, prefix="primeros_dias")
        datos_alimentacion = AlimentacionForm(request.POST, prefix="alimentacion")
        suplementos_formset = SuplementosFormset(request.POST, instance=AlimentacionCostumbres())
        datos_familiares = DatosFamiliaresOtrosForm(request.POST, prefix="familiares_otros")
        hermanos_formset = HermanosFormset(request.POST, instance=DatosFamiliaresOtros())

        if (datos_paciente.is_valid() and
            datos_familia.is_valid() and
            datos_medico.is_valid() and
            datos_descripcion_paciente.is_valid() and medicamento_formset.is_valid() and
            datos_historial_madre.is_valid() and
            datos_gestacion.is_valid() and
            datos_nacimiento.is_valid() and
            datos_recien_nacido.is_valid() and
            datos_primeros_dias.is_valid() and
            datos_alimentacion.is_valid() and suplementos_formset.is_valid() and
            datos_familiares.is_valid() and hermanos_formset.is_valid()):


            paciente = datos_paciente.save(commit=False)
            familiares_instances = datos_familia.save(commit=False)
            medicos_instances = datos_medico.save(commit = False)

            descripcion = datos_descripcion_paciente.save()
            medicamentos_instances = medicamento_formset.save(commit=False)
            for medicamento in medicamentos_instances:
                medicamento.descripcion = descripcion
                medicamento.save()

            historial_madre = datos_historial_madre.save()
            gestacion = datos_gestacion.save()
            for actividad_form in actividad_gestacion:
                if actividad_form.is_valid():
                    actividad = actividad_form.save(commit=False)
                    actividad.gestacion = gestacion
                    actividad.save()
            for situacion_form in situacion_gestacion:
                if situacion_form.is_valid():
                    situacion = situacion_form.save(commit=False)
                    situacion.gestacion = gestacion
                    situacion.save()

            nacimiento = datos_nacimiento.save()
            recien_nacido = datos_recien_nacido.save()
            primeros_dias = datos_primeros_dias.save()
            alimentacion = datos_alimentacion.save()
            familiares = datos_familiares.save()


            suplementos = suplementos_formset.save(commit=False)
            for suplemento in suplementos:
                suplemento.alimentacion = alimentacion
                suplemento.save()

            hermanos = hermanos_formset.save(commit=False)
            for hermano in hermanos:
                hermano.datos_familiares = familiares
                hermano.save()

            paciente.descripcion = descripcion
            paciente.historial_madre = historial_madre
            paciente.gestacion = gestacion
            paciente.nacimiento = nacimiento
            paciente.recien_nacido = recien_nacido
            paciente.primeros_dias = primeros_dias
            paciente.alimentacion = alimentacion
            paciente.datos_familiares = familiares

            paciente.save()

            for familiar in familiares_instances:
                familiar.paciente = paciente
                familiar.save()

            for medico in medicos_instances:
                medico.paciente = paciente
                medico.save()

            return HttpResponseRedirect('/')


        print "datos is invalid"
        print("Errors paciente:", datos_paciente.errors)
        print("Errors familiares:", datos_familia.errors)
        print("Errors medico:", datos_medico.errors)
        print ("Errors descripcion", datos_descripcion_paciente.errors)
        print("Errors historial madre", datos_historial_madre.errors)
        print("Errors gestacion", datos_gestacion.errors)
        print("Errors nacimiento:", datos_nacimiento.errors)
        print("Errors recien_nacido:", datos_recien_nacido.errors)
        print("Errors primeros_dias:", datos_primeros_dias.errors)
        print("Errors alimentacion:", datos_alimentacion.errors)
        print("Errors suplementos", suplementos_formset.errors)
        print("Errors DatosFamiliares", datos_familiares.errors)
        print("Errors Hermano", hermanos_formset.errors)
        return render(request, self.template_name,
                      {'ficha_datos_form': datos_paciente,
                       'datos_familia_formset': datos_familia,
                       'datos_medico_formset': datos_medico,
                       'descripcion_paciente': datos_descripcion_paciente,
                       'medicamento_formset':medicamento_formset,
                       'historial_madre_form': datos_historial_madre,
                       'gestacion': datos_gestacion,
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

