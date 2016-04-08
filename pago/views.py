from django.shortcuts import render, render_to_response

from django.db import connection

import json
from django.http import HttpResponse


# Create your views here.
def index_view(request):
  return render(request, 'pago/index.html')

def patient_payments(request, patientId):
  cursor = connection.cursor()
  cursor.execute("select p.nombres, p.apellidos, t.nombre as terapia_nombre, t.tiempo, c.hora_inicio, c.hora_fin, c.fecha_cita, t.costo from registro_paciente p left join cita_cita c on p.id = c.paciente_id left join asistencia_tipo_terapia t on c.tipo_terapia_id = t.id where p.id = %s", [patientId])
  row = cursor.fetchall()
  return HttpResponse(json.dumps(row), content_type='application/json')
  

