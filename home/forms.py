from django import forms
#from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))


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
    #password = forms.CharField(widget=forms.PasswordInput(render_value=False))