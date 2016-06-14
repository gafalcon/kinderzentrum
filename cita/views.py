from django.contrib.auth.decorators                     import login_required
from django.forms                                       import formset_factory
from django.http                                        import HttpResponseRedirect
from django.shortcuts                                   import render, render_to_response
from django.template                                    import RequestContext
from django.utils.decorators                            import method_decorator
from django.views.generic                               import View
from modelos.cita_model                                 import Cita
from asistencia.modelos.Terapista_model                 import Terapista
from asistencia.modelos.Tipo_terapia_model              import Tipo_terapia
from asistencia.modelos.Terapia__Tipo_terapia_models    import Terapia__Tipo_terapia
from registro.modelos.paciente_model                    import Paciente


@method_decorator(login_required, name="dispatch")
class ReservarCitaView(View):
    template_name = 'cita/reservar_cita.html'

    template_name = 'cita/reservar_cita.html'
    def get(self, request, *args, **kwargs):
        pacientes = Paciente.objects.order_by('fecha_registro')
        tipo_terapia_list = Tipo_terapia.objects.order_by('costo')
        terapista_list = Terapista.objects.order_by('fecha_nacimiento')
        return render(request,self.template_name,{'pacientes':pacientes, 'tipo_terapia_list':tipo_terapia_list, 'terapista_list':terapista_list, 'pagina_actual': 'cita'})

    def post(self, request, *args, **kwargs):
        fechacita = request.POST.get('date_holder', default = "")
        horaini = request.POST.get('horainicio', default = "")

        if horaini == "08:00 am":
            horaini = "08:00:00"        
        elif horaini == "08:30 am":
            horaini = "08:30:00"        
        elif  horaini == "09:00 am":
            horaini = "09:00:00"
        if horaini == "09:30 am":
            horaini = "09:30:00"        
        elif horaini == "10:00 am":
            horaini = "10:00:00"        
        elif  horaini == "10:30 am":
            horaini = "10:30:00"
        if horaini == "11:00 am":
            horaini = "11:00:00"        
        elif horaini == "11:30 am":
            horaini = "11:30:00"        
        elif  horaini == "12:00 pm":
            horaini = "12:00:00"
        elif  horaini == "12:30 pm":
            horaini = "12:30:00"
        if horaini == "01:00 pm":
            horaini = "13:00:00"        
        elif horaini == "01:30 pm":
            horaini = "13:30:00"        
        elif  horaini == "02:00 pm":
            horaini = "14:00:00"
        if horaini == "02:30 pm":
            horaini = "14:30:00"        
        elif horaini == "03:00 pm":
            horaini = "15:00:00"
        elif horaini == "03:30 pm":
            horaini = "15:30:00"        
        elif  horaini == "04:00 pm":
            horaini = "16:00:00"
        if horaini == "04:30 pm":
            horaini = "16:30:00"        
        elif horaini == "05:00 pm":
            horaini = "17:00:00"        
        elif  horaini == "05:30 pm":
            horaini = "17:30:00"
        elif horaini == "06:00 pm":
            horaini = "18:00:00"        
        elif  horaini == "06:30 pm":
            horaini = "18:30:00"


        horafin = request.POST.get('horafin', default = "")

        if horafin == "08:00 am":
            horafin = "08:00:00"       
        elif horafin == "08:30 am":
            horafin = "08:30:00"        
        elif  horafin == "09:00 am":
            horafin = "09:00:00"
        if horafin == "09:30 am":
            horafin = "09:30:00"        
        elif horafin == "10:00 am":
            horafin = "10:00:00"        
        elif  horafin == "10:30 am":
            horafin = "10:30:00"
        if horafin == "11:00 am":
            horafin = "11:00:00"        
        elif horafin == "11:30 am":
            horafin = "11:30:00"        
        elif  horafin == "12:00 pm":
            horafin = "12:00:00"
        elif  horafin == "12:30 pm":
            horafin = "12:30:00"
        if horafin == "01:00 pm":
            horafin = "13:00:00"        
        elif horafin == "01:30 pm":
            horafin = "13:30:00"        
        elif  horafin == "02:00 pm":
            horafin = "14:00:00"
        if horafin == "02:30 pm":
            horafin = "14:30:00" 
        elif horafin == "03:00 pm":
            horafin = "15:00:00"       
        elif horafin == "03:30 pm":
            horafin = "15:30:00"        
        elif  horafin == "04:00 pm":
            horafin = "16:00:00"
        if horafin == "04:30 pm":
            horafin = "16:30:00"        
        elif horafin == "05:00 pm":
            horafin = "17:00:00"        
        elif  horafin == "05:30 pm":
            horafin = "17:30:00"
        elif horafin == "06:00 pm":
            horafin = "18:00:00"        
        elif  horafin == "06:30 pm":
            horafin = "18:30:00"
        paciente_id = request.POST.get('paciente', default = "")
        tipoterapia_id = request.POST.get('tipoterapia', default = "")
        terapista_id = request.POST.get('terapista', default = "")
        cita = Cita()
        try:
            cita.tipo_terapia = Tipo_terapia.objects.get(id=tipoterapia_id)
        except Tipo_terapia.DoesNotExist:
            print "error"
        try:
            cita.paciente = Paciente.objects.get(id=paciente_id)
        except Paciente.DoesNotExist:
            print "error"
        try:
            cita.terapista = Terapista.objects.get(id=terapista_id)
        except Terapista.DoesNotExist:
            print "error"
        cita.fecha_cita=fechacita
        cita.hora_inicio=horaini
        cita.hora_fin=horafin
        #cita = Cita(fecha_cita=fechacita,  hora_inicio=horaini, hora_fin=horafin, tipo_terapia=tipoterapia, paciente=paciente, terapista=terapista)
        cita.save()
        return render(request, self.template_name, {'pagina_actual': 'cita'})
        return HttpResponseRedirect('/cita')