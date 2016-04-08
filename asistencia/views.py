import json
from django.db import connection
from django.shortcuts import render, render_to_response,get_list_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.template import RequestContext
from modelos.bebe_model import Bebe
from modelos.cit_model import Cit
from modelos.terapia_model import Terapia


def mostrar_lista_asistencia(request):
    #template_name = 'cita/reservar_cita.html'

    #pacientes = get_list_or_404(Bebe)
    #return render_to_response('asistencia/mostrar_lista.html',{'pacientes':pacientes})

    bebe_terapia = Bebe.objects.select_related()
    cita = Cit.objects.select_related()

    cursor = connection.cursor()
    cursor.execute('SELECT paciente.id as idPaciente, '
                         '(paciente.nombres+paciente.apellidos) as paciente, '
                         'tipoT.nombre as tipoTerapia, '
                         'case cita.estado '
                         'when \'A\' then \'Agendado\' '
                         'when \'S\' then \'Asistio\' '
                         'when \'N\' then \'No asistio\' '
                         'when \'C\' then \'Cancelado\' '
                         'END as estado '
                         'from asistencia_tipo_terapia as tipoT, registro_paciente as paciente, cita_cita as cita '
                         'where tipoT.id = cita.tipo_terapia_id and paciente.id = cita.paciente_id')
    #tabla_pacientes = Bebe.objects.raw()

    '''r = query_to_dicts("""SELECT b.id as id,
                         b.nombre as bebe,
                         t.nombre as terapia,
                         case cit.estado
                         when \'A\' then \'Agendado\'
                         when \'S\' then \'Asistio\'
                         when \'N\' then \'No asistio\'
                         when \'C\' then \'Cancelado\'
                         END as estado
                         from asistencia_terapia as t , asistencia_bebe as b , asistencia_cit as cit
                         where t.id = b.terapia_id and b.id = cit.bebe_id""")'''
    ro = dictfetchall(cursor)
    row = json.dumps(ro)

    print(row)
    ctx = {'paciente': row, 'pagina_actual':'asistencia_paciente'}
    #print(dictfetchall(cursor))
    return render(request, "asistencia/mostrar_lista.html", ctx)
    #return render_to_response('asistencia/mostrar_lista.html')


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    list = [dict(zip(columns,row))for row in cursor.fetchall()]
    return list
