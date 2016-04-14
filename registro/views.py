from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from registro.forms import *
from django.template import RequestContext
from registro.modelos.paciente_model import Paciente
from registro.modelos.familiars_models import DatosFamiliaresOtros, Familiar
from registro.modelos.alimentacion_models import AlimentacionCostumbres
from registro.modelos.recien_nacido_model import RecienNacido
from registro.modelos.medico_model import Medico
from registro.modelos.historial_madre_models import Actividad_Gestacion, Situacion_Gestacion
from django.http import HttpResponseRedirect
from django.views.generic import View, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.forms import formset_factory
# Create your views here.



@method_decorator(login_required, name="dispatch")
class RegistroView(View):
    template_name = 'registro/registro_ficha_medica.html'
    def get(self, request, *args, **kwargs):
        datos = PacienteForm(prefix="paciente")
        datos_familia = DatosFamiliaresFormset(prefix="familiares", queryset=Familiar.objects.none())
        datos_medico = DatosMedicoFormset(prefix="medico", queryset=Medico.objects.none())

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

            return redirect('pacientes-list')


        # print "datos is invalid"
        # print("Errors paciente:", datos_paciente.errors)
        #print("Errors familiares:", datos_familia.errors)
        # print("Errors medico:", datos_medico.errors)
        # print ("Errors descripcion", datos_descripcion_paciente.errors)
        # print("Errors historial madre", datos_historial_madre.errors)
        # print("Errors gestacion", datos_gestacion.errors)
        # print("Errors nacimiento:", datos_nacimiento.errors)
        # print("Errors recien_nacido:", datos_recien_nacido.errors)
        # print("Errors primeros_dias:", datos_primeros_dias.errors)
        # print("Errors alimentacion:", datos_alimentacion.errors)
        # print("Errors suplementos", suplementos_formset.errors)
        # print("Errors DatosFamiliares", datos_familiares.errors)
        # print("Errors Hermano", hermanos_formset.errors)
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


@method_decorator(login_required, name="dispatch")
class PacienteListView(ListView):
    model = Paciente

    def get_context_data(self, **kwargs):
        context = super(PacienteListView, self).get_context_data(**kwargs)
        context['pagina_actual'] = 'registro'
        return context

   
class RegistroEditView(View):
    template_name = 'registro/registro_ficha_medica.html'

    def init_historial_madre_form(self, historial_madre):
        enf_previas = historial_madre.enfermedades_previas.split(',')
        otra_enf_previa = enf_previas[-1] if 'otra' in enf_previas else ''
        enf_emb = historial_madre.enfermedades_durante_embarazo.split(',')
        otra_enf_emb = enf_emb[-1] if 'otra' in enf_emb else ''
        tuvo_defuncion_fetal = "True" if historial_madre.defunciones_fetales > 0 else "False"
        tuvo_hijos_muertos = "True" if historial_madre.hijos_nacidos_muertos > 0 else "False"
        anticonceptivos = historial_madre.anticonceptivos.split(',')
        uso_anticonceptivo = "True" if anticonceptivos else "False"
        initial = {
            'enfermedades_previas': enf_previas,
            'otra_enf_previa': otra_enf_previa,
            'enfermedades_durante_embarazo': enf_emb,
            'otra_enf_embarazo': otra_enf_emb,
            'tuvo_defuncion_fetal': tuvo_defuncion_fetal,
            'tuvo_hijos_muertos': tuvo_hijos_muertos,
            'anticonceptivos': anticonceptivos,
            'uso_anticonceptivo': uso_anticonceptivo
        }
        return HistorialMadreForm(prefix="historial_madre",
                                  instance=historial_madre,
                                  initial=initial)
        

    def init_gestacion_form(self, gestacion):
        sentimientos = gestacion.sentimientos.split(',')
        comun = gestacion.comunicacion_bebe.split(',')
        curso_prenatal = "True" if gestacion.lugar_curso_prenatal != '' else "False"
        initial = {
            'curso_prenatal': curso_prenatal,
            'sentimientos': sentimientos,
            'comunicacion_bebe': comun
        }
        return DesarrolloDeLaGestacionForm(prefix="gestacion",
                                           instance=gestacion,
                                           initial=initial)


    def init_nacimiento_form(self, nacimiento):
        complicaciones = nacimiento.complicaciones.split(',')
        metodo = nacimiento.metodo_nacimiento.split(',')
        print 'metodo', metodo
        initial = {
            'complicaciones': complicaciones,
            'metodo_nacimiento': metodo
        }
        return NacimientoForm(prefix="nacimiento",
                              instance=nacimiento,
                              initial=initial)


    def init_recien_nacido_form(self, recien_nacido):
        comp_nacimiento = recien_nacido.complicaciones_nacimiento.split(',')
        otra_complicacion = comp_nacimiento[-1] if 'Otro' in comp_nacimiento else ''
        tiempo_internado = recien_nacido.tiempo_internado
        hubo_apego_precoz = 'False' if recien_nacido.tiempo_apego_precoz == RecienNacido.APEGO_PRECOZ_NADA else 'True'
        print "tiempo internado", tiempo_internado, type(tiempo_internado)
        initial = {
            'complicaciones_nacimiento': comp_nacimiento,
            'otra_complicacion': otra_complicacion,
            'hubo_apego_precoz': hubo_apego_precoz
        }
        return RecienNacidoForm(prefix="recien_nacido",
                                instance=recien_nacido,
                                initial=initial)
    
    def get(self, request, *args, **kwargs):
        id_paciente = kwargs.get('id_paciente')

        paciente = get_object_or_404(Paciente, pk=id_paciente)
        datos = PacienteForm(prefix="paciente", instance=paciente)
        datos_familia = DatosFamiliaresFormset(prefix="familiares",
                                               queryset=Familiar.objects.filter(paciente=paciente))
        datos_medico = DatosMedicoFormset(prefix="medico",
                                          queryset=Medico.objects.filter(paciente=paciente))

        historial_madre = self.init_historial_madre_form(paciente.historial_madre)

        descripcion = paciente.descripcion
        areas_dificultad = descripcion.areas_dificultad.split(',')
        otra_area = areas_dificultad[-1] if 'otro' in areas_dificultad else ''
        print 'otra area', otra_area
            
        descripcion_paciente = DescripcionPacienteForm(prefix="descripcion_paciente",
                                                       instance=descripcion,
                                                       initial={
                                                           'areas_dificultad': areas_dificultad,
                                                           'otro_dificultad': otra_area
                                                       }
        )
        #assert False
        medicamento_formset = MedicamentoFormset(instance=Descripcion())
        gestacion = self.init_gestacion_form(paciente.gestacion)
        actividad_gestacion = ActividadGestacionFormset(prefix="actividad",
                                                        initial=[{'nombre_actividad':x} for x in Actividad_Gestacion.ACTIVIDADES_CHOICES])
        situacion_gestacion = SituacionGestacionFormset(prefix="situacion",
                                                        initial=[{'nombre_situacion':x} for x in Situacion_Gestacion.SITUACIONES_CHOICES])
        nacimiento = self.init_nacimiento_form(paciente.nacimiento)
        datos_recien_nacido = self.init_recien_nacido_form(paciente.recien_nacido)
        primeros_dias = PrimerosDiasForm(prefix="primeros_dias", initial={'icteria': False}, instance=paciente.primeros_dias)
        alimentacion = AlimentacionForm(prefix="alimentacion", instance=paciente.alimentacion)
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
        print "POST edit paciente"
        id_paciente = kwargs.get('id_paciente')
        paciente = get_object_or_404(Paciente, pk=id_paciente)
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

            return redirect('pacientes-list')

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
