from django.shortcuts import render, render_to_response,get_list_or_404
from cita.forms import Ficha_DatosForm
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.template import RequestContext
from registro.modelos.paciente_model import Paciente
from asistencia.pacienteTable import PacienteTable


def mostrar_lista_asistencia(request):
    #template_name = 'cita/reservar_cita.html'

    #pacientes = get_list_or_404(Paciente)
    #return render_to_response('asistencia/mostrar_lista.html',{'pacientes':pacientes})

    paciente = PacienteTable()

    return render(request, "asistencia/mostrar_lista.html", {'paciente': paciente})
    #return render_to_response('asistencia/mostrar_lista.html')