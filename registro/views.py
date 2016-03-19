from django.shortcuts import render, render_to_response
from registro.forms import * #Ficha_DatosForm, Ficha_DatosFamiliaresForm, Ficha_DatosMedicoForm, HistorialMadreForm
from django.template import RequestContext
from registro.modelos.familiars_models import DatosFamiliaresOtros
from registro.modelos.alimentacion_models import AlimentacionCostumbres
from django.http import HttpResponseRedirect

# Create your views here.
def registro_view(request):
    mensaje = ""
    if request.method == "POST":
        mensaje = "guardando datos"
        #print(request.POST)
        datos = Ficha_PacienteForm(request.POST, prefix="paciente")
        datos_medico = Ficha_DatosMedicoForm(request.POST, prefix="medico")
        datos_familia = Ficha_DatosFamiliaresForm(request.POST, prefix="familiares")
        if datos.is_valid() and datos_medico.is_valid() and datos_familia.is_valid():
            print("datos is valid")
            print("Paciente", datos.cleaned_data)
            print("Medico", datos_medico.cleaned_data)
            print("Familiares", datos_familia.cleaned_data)
        else:
            print("datos is invalid")
            print("Paciente", datos.cleaned_data)
            print("Medico", datos_medico.cleaned_data)
            #print("Familiares", datos_familia.cleaned_data)
            print("\n\nErrors paciente:", datos.errors)
            print("\n\nErrors medico:", datos_medico.errors)
            print("\n\nErrors familiares:", datos_familia.errors)
            print(datos)
            return render(request, 'registro/registro_ficha_medica.html',
                          {'ficha_datos_form': datos,
                           'ficha_datos_familia_form': datos_familia,
                           'ficha_datos_medico_form': datos_medico
                          })
        return HttpResponseRedirect('/')
    else:
        mensaje = "enviando forma"
   #datos 
    datos = Ficha_PacienteForm(prefix="paciente")
    print(datos)
    datos_familia = Ficha_DatosFamiliaresForm(prefix="familiares")
    datos_medico = Ficha_DatosMedicoForm(prefix="medico")
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
    return render(request, 'registro/registro_ficha_medica.html', ctx)

