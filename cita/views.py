from django.contrib.auth.decorators import login_required
from django.forms                   import formset_factory
from django.http                    import HttpResponseRedirect
from django.shortcuts               import render, render_to_response
from django.template                import RequestContext
from django.utils.decorators        import method_decorator
from django.views.generic           import View
from .forms                         import *
from .modelos.cita_model            import Cita


@method_decorator(login_required, name="dispatch")
class ReservarCitaView(View):
    template_name = 'cita/reservar_cita.html'

    def get(self, request, *args, **kwargs):
        cita = CitaForm(prefix="cita")
        context = {'cita_form': cita,
        		   'pagina_actual': 'cita'}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        c = {}
        c.update(csrf(request))

        if (not request.user.is_authenticated()) or (request.user == None):
            return HttpResponseRedirect("/admin/")
        
        form = c['CitaForm'] = CitaForm(request.POST, c, context_instance=RequestContext(request))

        if c['CitaForm'].is_valid():
            return HttpResponseRedirect("/cita")

        else:
            form = c['CitaForm'] = CitaForm()
        return render_to_response(self.template_name, {'form': c['CitaForm']})






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