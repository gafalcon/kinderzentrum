from django.shortcuts import render, render_to_response

from django.db import connection

# Create your views here.
def index_view(request):
  return render(request, 'pago/index.html')

def patient_payments(request, patientId):
  cursor = connection.cursor()
  cursor.execute("SELECT p.*, c.*, t.* FROM kinderzentrum_terapia t inner join kinderzentrum_terapista m on t.id = m.terapia inner join kinderzentrum_cita c on m.id = c.terapista_id inner join kinderzentrum_paciente p on p.id = c.paciente_id where p.id = %s", [patientId])
  row = cursor.fetchall()
  return row
  

