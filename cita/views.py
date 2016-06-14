from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .modelos.cita_model import Cita
#from django.utils.decorators import method_decorator


class ReservarCitaView(View):
    template_name = 'cita/reservar_cita.html'

    def get(self, request, *args, **kwargs):
        context = {'pagina_actual': 'cita'}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {'pagina_actual': 'cita'}
        return render(request, self.template_name, context)
        return HttpResponseRedirect('/cita')