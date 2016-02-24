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

class Ficha_DatosFamiliaresForm(forms.Form):
    ESTUDIO=[('primaria','Primaria'),('secundaria','Secundaria'),('universitaria','Universitaria'),('superior','Superior')]
    apellidos = forms.CharField(widget=forms.TextInput())
    nombres = forms.CharField(widget=forms.TextInput())
    parentesco = forms.CharField(widget=forms.TextInput())
    nivel_estudio = forms.ChoiceField(choices=ESTUDIO)
    #trabajo
    empresa = forms.CharField(widget=forms.TextInput())
    direccion = forms.CharField(widget=forms.TextInput())
    empresa = forms.CharField(widget=forms.TextInput())
    #domicilio
    direccion_domicilio = forms.CharField(widget=forms.TextInput())
    telefono = forms.CharField(widget=forms.TextInput())

class Ficha_DatosMedicoForm(forms.Form):
    apellidos = forms.CharField(widget=forms.TextInput())
    nombres = forms.CharField(widget=forms.TextInput())
    area = forms.CharField(widget=forms.TextInput())
    direccion = forms.CharField(widget=forms.TextInput())
    telefono = forms.CharField(widget=forms.TextInput())
        

        
