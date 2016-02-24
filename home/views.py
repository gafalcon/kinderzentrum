# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.template import RequestContext
from home.forms import LoginForm, Ficha_DatosForm

# Create your views here.


def index_view(request):
    if request.user.is_authenticated():
        grupos = request.user.groups.all()
        '''
        Aqui vamos a colocar las condiciones para que se habiliten las condiciones que el usuario
        va a usar
        '''
        registro = grupos.filter(name='registro').count() == 1
        ctx = {'registro':registro}
        return render_to_response('base.html', ctx, context_instance=RequestContext(request))
    else:
        return render_to_response('base.html', context_instance=RequestContext(request))

def formulario_view(request):
	return render_to_response('registro/formulario.html', context_instance=RequestContext(request))

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


def ficha_view(request):
	if request.method == "POST":
		form = FichaForm(request.POST)

    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


'''WEBADAS DE REGISTRO'''
def registro_view(request):
    mensaje = ""
    if request.method == "POST":
        mensaje = "guardando datos"
    else:
        mensaje = "enviando forma"
    datos = Ficha_DatosForm()
    ctx = {'ficha_datos_form':datos,'mensaje':mensaje}
    return render_to_response('home/registro_ficha_medica.html',ctx,context_instance=RequestContext(request))
