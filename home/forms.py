# -*- encoding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
import datetime
#from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Usuario','autofocus':'autofocus'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Contraseña'}))


        
class RegistroUsuario(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombres','autofocus':'autofocus'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apellidos'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Contraseña'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Contraseña'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'email@email.com'}))
        
