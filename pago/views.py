from django.shortcuts import render, render_to_response

from django.db import connection

import json
from django.http import HttpResponse

from django.core.serializers.json import DjangoJSONEncoder

import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index_view(request):
  return render(request, 'pago/index.html')

def patient_payments(request, patientId):
    cursor = connection.cursor()
    cursor.execute("select p.nombres, p.apellidos, t.nombre as terapia_nombre, t.tiempo, c.hora_inicio, c.hora_fin, c.fecha_cita, t.costo from registro_paciente p left join cita_cita c on p.id = c.paciente_id left join asistencia_tipo_terapia t on c.tipo_terapia_id = t.id where p.id = \'%s\'", [patientId])
    row = dictfetchall(cursor)
    return HttpResponse(json.dumps(row, cls=DjangoJSONEncoder), content_type='application/json')

def patient_suggestions(request):
    query = request.GET.get('query', '').strip()
    logger.debug(query)
    limit = request.GET.get('limit', '5')
    if (query == ''):
        return HttpResponse(json.dumps([]), content_type='application/json')
    cursor = connection.cursor()
    cursor.execute("select p.id, p.nombres, p.apellidos from registro_paciente p where p.nombres like \'%{0}%\' or p.apellidos like \'%{0}%\' limit {1}".format(query, limit))
    row = dictfetchall(cursor)
    return HttpResponse(json.dumps(row), content_type='application/json')

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
