from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from registro.forms import *
from django.template import RequestContext
from registro.modelos.paciente_model import Paciente
from registro.modelos.familiars_models import DatosFamiliaresOtros, Familiar
from registro.modelos.alimentacion_models import AlimentacionCostumbres
from registro.modelos.recien_nacido_model import RecienNacido
from registro.modelos.medico_model import Medico
from registro.modelos.historial_madre_models import Actividad_Gestacion, Situacion_Gestacion
from registro.modelos.descripcion_models import Terapia
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
        uso_anticonceptivo = "True" if anticonceptivos[0] != '' else "False"
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
        medicamento = "None" if nacimiento.medicamentos_parto is None else nacimiento.medicamentos_parto
        cordon = "None" if nacimiento.complicaciones_cordon is None else nacimiento.complicaciones_cordon
        initial = {
            'complicaciones': complicaciones,
            'metodo_nacimiento': metodo,
            'medicamentos_parto': medicamento,
            'complicaciones_cordon': cordon
        }
        return NacimientoForm(prefix="nacimiento",
                              instance=nacimiento,
                              initial=initial)


    def init_recien_nacido_form(self, recien_nacido):
        comp_nacimiento = recien_nacido.complicaciones_nacimiento.split(',')
        otra_complicacion = comp_nacimiento[-1] if 'Otro' in comp_nacimiento else ''
        tiempo_internado = recien_nacido.tiempo_internado
        hubo_apego_precoz = 'False' if recien_nacido.tiempo_apego_precoz == RecienNacido.APEGO_PRECOZ_NADA else 'True'
        permanecio_internado = 'False' if tiempo_internado == datetime.timedelta() else 'True'
        initial = {
            'complicaciones_nacimiento': comp_nacimiento,
            'otra_complicacion': otra_complicacion,
            'hubo_apego_precoz': hubo_apego_precoz,
            'permanecio_internado': permanecio_internado
        }
        return RecienNacidoForm(prefix="recien_nacido",
                                instance=recien_nacido,
                                initial=initial)

    def init_primeros_dias_form(self, primeros_dias):
        examenes = primeros_dias.examenes.split(',')
        situaciones = primeros_dias.situaciones_despues_nacimiento.split(',')
        initial = {
            'clinica': 'True' if primeros_dias.clinica_permanencia else 'False',
            'situaciones_despues_nacimiento': situaciones,
            'icteria': 'None' if primeros_dias.icteria is None else primeros_dias.icteria,
            'otro_examen': examenes[-1] if 'Otro' in examenes else '',
            'examenes': examenes,
            'otra_situacion': situaciones[-1] if 'Otro' in situaciones else '',
            'dormia_toda_noche': 'True' if primeros_dias.veces_despertar_noche == 0 else 'False'
        }
        return PrimerosDiasForm(prefix="primeros_dias",
                                initial=initial,
                                instance=primeros_dias)

    def init_alimentacion_form(self, alimentacion, suplementos):

        motivo_suspencion = [] if alimentacion.motivo_suspencion_lactancia is None else alimentacion.motivo_suspencion_lactancia.split(',')
        afecciones = alimentacion.afecciones.split(',')
        enfs = alimentacion.enfermedades.split(',')
        forma_alim = alimentacion.forma_alimento.split(',')
        initial = {
            'lactancia': 'True' if motivo_suspencion else 'False',
            'motivo_suspencion_lactancia': motivo_suspencion,
            'otro_motivo_suspencion_lactancia': motivo_suspencion[-1] if 'Otro' in motivo_suspencion else '',
            'afecciones': afecciones,
            'otra_afeccion': afecciones[-1] if 'Otros' in afecciones else '',
            'otra_enfermedad': enfs[-1] if 'Otro' in enfs else '',
            'enfermedades': enfs,
            'otra_forma_alimento': forma_alim[-1] if 'Otro' in forma_alim else '',
            'forma_alimento': forma_alim,
            'difiere_alimentacion': 'True' if alimentacion.motivo_cambios_alimentacion else 'False',
            'suplementos': suplementos
        }
        return AlimentacionForm(prefix="alimentacion",
                                initial=initial,
                                instance=alimentacion)
    
    def init_historia_familiar_form(self, historia_familiar):
        orientador = historia_familiar.orientacion_a_institucion.split(',')
        initial = {
            'transtorno_hermanos': 'None' if historia_familiar.transtorno_hermanos is None else historia_familiar.transtorno_hermanos,
            'alteracion_desarrollo':'None' if historia_familiar.alteracion_desarrollo is None else historia_familiar.alteracion_desarrollo,
            'otro_orientador': orientador[-1] if 'Otro' in orientador else '',
            'orientacion_a_institucion': orientador[0]
        }
        return  DatosFamiliaresOtrosForm(prefix="familiares_otros",
                                         initial=initial,
                                         instance=historia_familiar)

    
    def init_descripcion_form(self, descripcion):
        areas_dificultad = descripcion.areas_dificultad.split(',')
        otra_area = areas_dificultad[-1] if 'otro' in areas_dificultad else ''
        terapias = descripcion.terapias
        terapias_reh_fisica = terapias.filter(tipo=1)
        terapias_est_temprana = terapias.filter(tipo=2)
        disc_molestias = descripcion.disc_molestias.split(',')
        tipo_terapia = []
        if len(terapias_reh_fisica):
            tipo_terapia.append("1")
        if len(terapias_est_temprana):
            tipo_terapia.append("2")
        if not tipo_terapia:
            tipo_terapia.append("3")
        initial={
            'areas_dificultad': areas_dificultad,
            'otro_dificultad': otra_area,
            'tipo_terapia': tipo_terapia,
            'tiempo_rehab_fisica': terapias_reh_fisica[0].tiempo_terapia if len(terapias_reh_fisica) else '',
            'tiempo_estimu_temprana': terapias_est_temprana[0].tiempo_terapia if len(terapias_est_temprana) else '',
            'disc_molestias': disc_molestias[0],
            'otro_disc_molestias': disc_molestias[-1] if len(disc_molestias) > 1 else ''
        }
        return DescripcionPacienteForm(prefix="descripcion_paciente",
                                       initial=initial,
                                       instance=descripcion,
        )

    def init_actividades(self, actividades):
        def find_periodo_a(name):
            for entry in actividades:
                if entry.nombre_actividad == name:
                    return entry.periodo 
            return ''       
        initial=[
            {'nombre_actividad':x,
             'periodo': find_periodo_a(x)} for x in Actividad_Gestacion.ACTIVIDADES_CHOICES]
        return ActividadGestacionFormset(prefix="actividad", initial=initial)

    def init_situaciones(self, situaciones ):
        def find_periodo_s(name):
            for entry in situaciones:
                if entry.nombre_situacion== name:
                    return entry.periodo 
            return ''
        initial=[
            {'nombre_situacion':x,
             'periodo': find_periodo_s(x)} for x in Situacion_Gestacion.SITUACIONES_CHOICES]
        return SituacionGestacionFormset(prefix="situacion", initial=initial)


    def get(self, request, *args, **kwargs):
        id_paciente = kwargs.get('id_paciente')

        paciente = get_object_or_404(Paciente, pk=id_paciente)
        datos = PacienteForm(prefix="paciente", instance=paciente)
        datos_familia = DatosFamiliaresFormset(prefix="familiares",
                                               queryset=Familiar.objects.filter(paciente=paciente))
        datos_medico = DatosMedicoFormset(prefix="medico",
                                          queryset=Medico.objects.filter(paciente=paciente))

        historial_madre = self.init_historial_madre_form(paciente.historial_madre)

        descripcion_paciente = self.init_descripcion_form(paciente.descripcion)
        medicamento_formset = MedicamentoFormset(instance=paciente.descripcion)
        gestacion = self.init_gestacion_form(paciente.gestacion)

        actividad_gestacion = self.init_actividades(paciente.gestacion.actividad_gestacion_set.all())
        situacion_gestacion = self.init_situaciones(paciente.gestacion.situacion_gestacion_set.all())

        nacimiento = self.init_nacimiento_form(paciente.nacimiento)
        datos_recien_nacido = self.init_recien_nacido_form(paciente.recien_nacido)
        primeros_dias = self.init_primeros_dias_form(paciente.primeros_dias)
        suplementos = paciente.alimentacion.suplementos
        alimentacion = self.init_alimentacion_form(paciente.alimentacion, 'True' if suplementos.count() else 'False')
        suplementos_formset = SuplementosFormset(instance=paciente.alimentacion)
        datos_familiares = self.init_historia_familiar_form(paciente.datos_familiares)
        hermanos_formset = HermanosFormset(instance=paciente.datos_familiares)
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
        datos_paciente = PacienteForm(request.POST, prefix="paciente", instance=paciente)
        datos_familia = DatosFamiliaresFormset(request.POST, prefix="familiares")
        datos_medico = DatosMedicoFormset(request.POST, prefix="medico")
        datos_historial_madre = HistorialMadreForm(request.POST, prefix="historial_madre", instance=paciente.historial_madre)
        datos_descripcion_paciente = DescripcionPacienteForm(request.POST, prefix="descripcion_paciente", instance=paciente.descripcion)
        medicamento_formset = MedicamentoFormset(request.POST, instance=Descripcion())
        datos_gestacion = DesarrolloDeLaGestacionForm(request.POST, prefix="gestacion", instance=paciente.gestacion)
        actividad_gestacion = ActividadGestacionFormset(request.POST, prefix="actividad")
        situacion_gestacion = SituacionGestacionFormset(request.POST, prefix="situacion")

        datos_nacimiento = NacimientoForm(request.POST, prefix="nacimiento", instance=paciente.nacimiento)
        datos_recien_nacido = RecienNacidoForm(request.POST, prefix="recien_nacido", instance=paciente.recien_nacido)
        datos_primeros_dias = PrimerosDiasForm(request.POST, prefix="primeros_dias", instance=paciente.primeros_dias)
        datos_alimentacion = AlimentacionForm(request.POST, prefix="alimentacion", instance=paciente.alimentacion)
        suplementos_formset = SuplementosFormset(request.POST, instance=AlimentacionCostumbres())
        datos_familiares = DatosFamiliaresOtrosForm(request.POST, prefix="familiares_otros", instance=paciente.datos_familiares)
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


            paciente = datos_paciente.save()
            # familiares_instances = datos_familia.save(commit=False)
            # medicos_instances = datos_medico.save(commit = False)

            descripcion = datos_descripcion_paciente.save()
            # medicamentos_instances = medicamento_formset.save(commit=False)
            # for medicamento in medicamentos_instances:
            #     medicamento.descripcion = descripcion
            #     medicamento.save()

            historial_madre = datos_historial_madre.save()
            # gestacion = datos_gestacion.save()
            # for actividad_form in actividad_gestacion:
            #     if actividad_form.is_valid():
            #         actividad = actividad_form.save(commit=False)
            #         actividad.gestacion = gestacion
            #         actividad.save()
            # for situacion_form in situacion_gestacion:
            #     if situacion_form.is_valid():
            #         situacion = situacion_form.save(commit=False)
            #         situacion.gestacion = gestacion
            #         situacion.save()

            nacimiento = datos_nacimiento.save()
            recien_nacido = datos_recien_nacido.save()
            primeros_dias = datos_primeros_dias.save()
            alimentacion = datos_alimentacion.save()
            familiares = datos_familiares.save()


            # suplementos = suplementos_formset.save(commit=False)
            # for suplemento in suplementos:
            #     suplemento.alimentacion = alimentacion
            #     suplemento.save()

            # hermanos = hermanos_formset.save(commit=False)
            # for hermano in hermanos:
            #     hermano.datos_familiares = familiares
            #     hermano.save()

            # for familiar in familiares_instances:
            #     familiar.paciente = paciente
            #     familiar.save()

            # for medico in medicos_instances:
            #     medico.paciente = paciente
            #     medico.save()

            return redirect('pacientes-list')
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
