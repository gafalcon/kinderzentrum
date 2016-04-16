from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View
from .forms import *
from .modelos.cita_model import Cita


@method_decorator(login_required, name="dispatch")
class ReservarCitaView(View):
    template_name = 'cita/reservar_cita.html'

    def get(self, request, *args, **kwargs):
        context = {'cita_form': CitaForm,
        		   'pagina_actual': 'cita'}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {'cita_form': CitaForm,
        		   'pagina_actual': 'cita'}
        return render(request, self.template_name, context)
        return HttpResponseRedirect('/cita')