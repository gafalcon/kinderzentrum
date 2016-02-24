# -*- encoding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
import datetime
#from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Usuario','autofocus':'autofocus'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Contraseña'}))


class Ficha_DatosForm(forms.Form):
    SEXO=[('masculino','Masculino'),('femenino','Femenino')]
    GRUPO_SANGUINEO = [('o+','O+'),('o-','O-'),('a+','A+'),('a-','A-'),('b+','B+'),('b-','B-'),('ab+','AB+'),('ab-','AB-')]
    apellidos = forms.CharField(widget=forms.TextInput())
    nombres = forms.CharField(widget=forms.TextInput())
    nacimiento = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
    sexo = forms.ChoiceField(choices=SEXO, widget=forms.RadioSelect())
    nacionalidad = forms.CharField(widget=forms.TextInput())
    lugar_nacimiento = forms.CharField(widget=forms.TextInput())
    grupo_sanguineo = forms.ChoiceField(choices=GRUPO_SANGUINEO)

class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
        
