import datetime

from cita.modelos.cita_model       import Cita
from django.contrib.auth.decorators import login_required
from django.forms                   import formset_factory
from django.http                    import HttpResponseRedirect
from django.shortcuts               import render, render_to_response
from django.template                import RequestContext
from django.utils.decorators        import method_decorator
from django.views.decorators.csrf   import csrf_exempt
from django.views.generic           import View
#from .forms                         import *
#from forms                      import CitaForm
from asistencia.modelos.Terapista_model                 import Terapista
from asistencia.modelos.Tipo_terapia_model              import Tipo_terapia
from asistencia.modelos.Terapia__Tipo_terapia_models    import Terapia__Tipo_terapia
from registro.modelos.paciente_model                    import Paciente
from django.core.urlresolvers import reverse
from django.core import serializers
from django.http import JsonResponse


@method_decorator(login_required, name="dispatch")
class ReservarCitaView(View):
	template_name = 'cita/reservar_cita.html'
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(ReservarCitaView, self).dispatch(request,*args,**kwargs)

	template_name = 'cita/reservar_cita.html'
	def get(self, request, *args, **kwargs):
		estados = Cita.ESTADO_CHOICES
		pacientes = Paciente.objects.order_by('fecha_registro')
		tipo_terapia_list = Tipo_terapia.objects.order_by('costo')
		terapista_list = Terapista.objects.order_by('fecha_nacimiento')
		return render(request,self.template_name,{'pacientes':pacientes, 'tipo_terapia_list':tipo_terapia_list, 'terapista_list':terapista_list, 'pagina_actual': 'cita','estados':estados})

	def post(self, request, *args, **kwargs):
		fechacita = request.POST.get('date_holder', default = "")
		annio = fechacita[8:]
		mes   = fechacita[0:3]
		dia   = fechacita[4:6]
		if   mes == "Ene":
			mes = "01"
		elif mes == "Feb":
			mes = "02"
		elif mes == "Mar":
			mes = "03"
		elif mes == "Abr":
			mes = "04"
		elif mes == "May":
			mes = "05"
		elif mes == "Jun":
			mes = "06"
		elif mes == "Jul":
			mes = "07"
		elif mes == "Ago":
			mes = "08"
		elif mes == "Sep":
			mes = "09"
		elif mes == "Oct":
			mes = "10"
		elif mes == "Nov":
			mes = "11"
		elif mes == "Dic":
			mes = "12"
		fechacita = annio + '-' + mes + '-' + dia
		horaini = request.POST.get('start', default = "")

		if horaini == "08:00 am":
			horaini = "08:00"
		elif horaini == "08:15 am":
			horaini = "08:15"
		elif horaini == "08:30 am":
			horaini = "08:30"
		elif horaini == "08:45 am":
			horaini = "08:45"
		elif  horaini == "09:00 am":
			horaini = "09:00"

		horafin = request.POST.get('end', default = "")

		if horafin == "08:00 am":
			horafin = "08:00"
		elif horafin == "08:15 am":
			horafin = "08:15"
		elif horafin == "08:30 am":
			horafin = "08:30"
		elif horafin == "08:45 am":
			horafin = "08:45"
		elif  horafin == "09:00 am":
			horafin = "09:00"

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
		cita.hora_inicio=datetime.datetime.strptime(horaini[:24],'%a %b %d %Y %H:%M:%S')
		cita.hora_fin=datetime.datetime.strptime(horafin[:24],'%a %b %d %Y %H:%M:%S')
		cita.save()

		return HttpResponseRedirect(reverse('reservar_cita_view'))





		# datos_cita = CitaForm(request.POST, prefix="cita")
		# if datos_cita.is_valid():
		#     #cita = datos_cita.save(commit=False) 
		#     cita.save() 
		#     print "datos de la cita grabados exitosamente"          
		#     context = {'cita_form': datos_cita,
		# 		       'pagina_actual': 'cita'}
		# #return render(request, self.template_name, context)
		# return render_to_response(self.template_name, context, context_instance=RequestContext(request))
		# #return render_to_response(self.template_name, context, RequestContext(request))
		# return HttpResponseRedirect('/cita')


def get_citas(request):
	if request.is_ajax():
		if request.method == 'GET':
			citas = Cita.objects.all().select_related()
			data = serializers.serialize('json', citas,indent=2,use_natural_foreign_keys=True, use_natural_primary_keys=True)
			return JsonResponse(data, safe=False)

	else:
		return redirect('/')


def get_cita(request):
	if request.is_ajax():
		if request.method == 'GET':
			cita_id = request.GET.get('id_cita',None)
			if cita_id:
				cita = Cita.objects.get(pk=cita_id)
				data = serializers.serialize('json',[cita,],indent=2,use_natural_foreign_keys=False, use_natural_primary_keys=True)
				return JsonResponse(data, safe=False)

			return JsonResponse({'success':False})

	else:
		return redirect('/')

def save_cita(request):
	if request.is_ajax():
		if request.method == 'POST':
			fechacita = request.POST.get('date_holder', default = "")
			annio = fechacita[8:]
			mes   = fechacita[0:3]
			dia   = fechacita[4:6]
			if  mes == "Ene":
				mes = "01"
			elif mes == "Feb":
				mes = "02"
			elif mes == "Mar":
				mes = "03"
			elif mes == "Abr":
				mes = "04"
			elif mes == "May":
				mes = "05"
			elif mes == "Jun":
				mes = "06"
			elif mes == "Jul":
				mes = "07"
			elif mes == "Ago":
				mes = "08"
			elif mes == "Sep":
				mes = "09"
			elif mes == "Oct":
				mes = "10"
			elif mes == "Nov":
				mes = "11"
			elif mes == "Dic":
				mes = "12"
			fechacita = annio + '-' + mes + '-' + dia
			horaini = request.POST.get('start', default = "")

			if horaini == "08:00 am":
				horaini = "08:00"
			elif horaini == "08:15 am":
				horaini = "08:15"
			elif horaini == "08:30 am":
				horaini = "08:30"
			elif horaini == "08:45 am":
				horaini = "08:45"
			elif  horaini == "09:00 am":
				horaini = "09:00"

			horafin = request.POST.get('end', default = "")

			if horafin == "08:00 am":
				horafin = "08:00"
			elif horafin == "08:15 am":
				horafin = "08:15"
			elif horafin == "08:30 am":
				horafin = "08:30"
			elif horafin == "08:45 am":
				horafin = "08:45"
			elif  horafin == "09:00 am":
				horafin = "09:00"

			paciente_id = request.POST.get('paciente', default =None)
			tipoterapia_id = request.POST.get('tipoterapia', default =None)
			terapista_id = request.POST.get('terapista', default =None)
			estado = request.POST.get('estado', default =None)
			indicaciones = request.POST.get('indicaciones', default =None)

			if paciente_id and tipoterapia_id and terapista_id and estado:
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
				cita.hora_inicio=datetime.datetime.strptime(horaini[:24],'%a %b %d %Y %H:%M:%S')
				cita.hora_fin=datetime.datetime.strptime(horafin[:24],'%a %b %d %Y %H:%M:%S')
				cita.estado = estado
				cita.indicaciones = indicaciones
				cita.save()
				return JsonResponse({'succes':True})
			else:
				return JsonResponse({'succes':False})

	else:
		return redirect('/')

def update_cita(request):
	if request.is_ajax():
		if request.method == 'POST':
			fechacita = request.POST.get('date_holder', default = "")
			annio = fechacita[8:]
			mes   = fechacita[0:3]
			dia   = fechacita[4:6]
			if  mes == "Ene":
				mes = "01"
			elif mes == "Feb":
				mes = "02"
			elif mes == "Mar":
				mes = "03"
			elif mes == "Abr":
				mes = "04"
			elif mes == "May":
				mes = "05"
			elif mes == "Jun":
				mes = "06"
			elif mes == "Jul":
				mes = "07"
			elif mes == "Ago":
				mes = "08"
			elif mes == "Sep":
				mes = "09"
			elif mes == "Oct":
				mes = "10"
			elif mes == "Nov":
				mes = "11"
			elif mes == "Dic":
				mes = "12"
			fechacita = annio + '-' + mes + '-' + dia
			horaini = request.POST.get('start', default = "")

			if horaini == "08:00 am":
				horaini = "08:00"
			elif horaini == "08:15 am":
				horaini = "08:15"
			elif horaini == "08:30 am":
				horaini = "08:30"
			elif horaini == "08:45 am":
				horaini = "08:45"
			elif  horaini == "09:00 am":
				horaini = "09:00"

			horafin = request.POST.get('end', default = "")

			if horafin == "08:00 am":
				horafin = "08:00"
			elif horafin == "08:15 am":
				horafin = "08:15"
			elif horafin == "08:30 am":
				horafin = "08:30"
			elif horafin == "08:45 am":
				horafin = "08:45"
			elif  horafin == "09:00 am":
				horafin = "09:00"

			cita_id = request.POST.get('cita_id',default=None)
			paciente_id = request.POST.get('paciente', default =None)
			tipoterapia_id = request.POST.get('tipoterapia', default =None)
			terapista_id = request.POST.get('terapista', default =None)
			estado = request.POST.get('estado', default =None)
			indicaciones = request.POST.get('indicaciones', default =None)

			if paciente_id and tipoterapia_id and terapista_id and estado and cita_id:
				cita = Cita.objects.all().filter(pk=cita_id).first()
				if cita:
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
					cita.hora_inicio=datetime.datetime.strptime(horaini[:24],'%a %b %d %Y %H:%M:%S')
					cita.hora_fin=datetime.datetime.strptime(horafin[:24],'%a %b %d %Y %H:%M:%S')
					cita.estado = estado
					cita.indicaciones = indicaciones
					cita.save(force_update=True)
					return JsonResponse({'succes':True})


			return JsonResponse({'succes':False})

		else:
			return JsonResponse({'succes':False})

	else:
		return redirect('/')

def delete_cita(request):
	if request.is_ajax():
		if request.method == 'POST':
			id_cita = request.POST.get('cita_id',None)
			if id_cita:
				Cita.objects.all().filter(pk=id_cita).delete()
				return JsonResponse({'succes':True})

			return JsonResponse({'succes':False})

	else:
		return redirect('/')