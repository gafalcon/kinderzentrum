# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.template import RequestContext
from home.forms import *
from django.views.generic import View

# Create your views here.


def index_view(request):
    if request.user.is_authenticated():
        grupos = request.user.groups.all()
        '''
        Aqui vamos a colocar las condiciones para que se habiliten las condiciones que el usuario
        va a usar
        '''
        registro = grupos.filter(name='registro').count() == 1
        ctx = {'registro':registro,'pagina_actual':'inicio'}
        return render(request, 'base.html', ctx)
    else:
        return render(request, 'base.html')


def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
    	#si esta autenticado redirecciona al formulario
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect('/')
                else:
                    mensaje = "Usuario y/o contraseña incorrecto"
        form = LoginForm()
        ctx = {'form':form,'mensaje':mensaje}
        return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')



class AdminUsuariosView(View):
    template_name = 'home/admin_usuarios.html'
    def get(self, request, *args, **kwargs):
        registro_usuario = RegistroUsuario()
        ctx = {'registro_usuario':registro_usuario}
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        registro_usuario = RegistroUsuario(request.POST)
        ctx = {'registro_usuario':registro_usuario}
        return render(request, self.template_name, ctx)


