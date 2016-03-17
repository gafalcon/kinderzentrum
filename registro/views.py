from django.shortcuts import render, render_to_response
from registro.forms import * #Ficha_DatosForm, Ficha_DatosFamiliaresForm, Ficha_DatosMedicoForm, HistorialMadreForm
from django.template import RequestContext
from registro.modelos.familiars_models import DatosFamiliaresOtros
from registro.modelos.alimentacion_models import AlimentacionCostumbres

# Create your views here.
def registro_view(request):
    mensaje = ""
    if request.method == "POST":
        mensaje = "guardando datos"
    else:
        mensaje = "enviando forma"
    #datos 
    datos = Ficha_PacienteForm()
    datos_familia = Ficha_DatosFamiliaresForm()
    datos_medico = Ficha_DatosMedicoForm()
    historial_madre = Ficha_HistorialMadreForm()
    #paciente = PacienteForm()
    #madre = MadreForm()
    #padre = PadreForm()
    descripcion_paciente = Ficha_DescripcionPacienteForm()
    recien_nacido = RecienNacidoForm()
    primeros_dias = PrimerosDiasForm()
    alimentacion = AlimentacionForm()
    suplementos_formset = SuplementosFormset(instance=AlimentacionCostumbres())
    datos_familiares = DatosFamiliaresOtrosForm()
    hermanos_formset = HermanosFormset(instance=DatosFamiliaresOtros())
    ctx = {'ficha_datos_medico_form':datos_medico,
           'ficha_datos_familia_form':datos_familia,
           'ficha_datos_form':datos,
           'descripcion_paciente':descripcion_paciente,
           'historial_madre_form': historial_madre,
           #'paciente': paciente,
           #'padre': padre,
           #'madre': madre,
           'mensaje':mensaje,
           'recien_nacido': recien_nacido,
           'alimentacion': alimentacion,
           'suplementos_formset': suplementos_formset,
           'datos_familiares': datos_familiares,
           'hermanos_formset': hermanos_formset,
           'primeros_dias': primeros_dias,
           'pagina_actual':'registro'}
    return render_to_response('registro/registro_ficha_medica.html',ctx,context_instance=RequestContext(request))
