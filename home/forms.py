# -*- encoding: utf-8 -*-
from django import forms
import datetime
#from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Contraseña'}))


class FichaForm(forms.Form):
    SEXO=[('masculino','Masculino'),('femenino','Femenino')]
    GRUPO_SANGUINEO = [('o+','O+'),('o-','O-')]
    apellidos = forms.CharField(widget=forms.TextInput())
    nombres = forms.CharField(widget=forms.TextInput())
    nacimiento = forms.DateField(initial=datetime.date.today)
    sexo = forms.ChoiceField(choices=SEXO, widget=forms.RadioSelect())
    nacionalidad = forms.CharField(widget=forms.TextInput())
    lugar_nacimiento = forms.CharField(widget=forms.TextInput())
    grupo_sanguineo = forms.CharField(widget=forms.TextInput())
