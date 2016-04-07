# -*- encoding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
#from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Usuario','autofocus':'autofocus'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Contraseña'}))


class UserCreateForm(UserCreationForm):
	password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Contraseña','class':'form-control'}))
	password2 = forms.CharField(label="Repita contraseña", widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Contraseña','class':'form-control'}))
	#grupos = forms.MultipleChoiceField(label='Seleccione permisos', required=True,  queryset=Group.objects.all())
	grupos = forms.ModelMultipleChoiceField(queryset=None,widget=forms.CheckboxSelectMultiple())

	def __init__(self, *args, **kw):  
	    super(UserCreateForm, self).__init__(*args, **kw)
	    self.fields['grupos'].queryset=Group.objects.all()

	class Meta:
		model = User
		fields = ('username', 'first_name' , 'last_name','email', 'password1', 'password2','grupos')
		widgets = {
				   'email': forms.EmailInput(attrs={'placeholder': 'email@email.com','class':'form-control'})
					}

	def save(self, commit=True):
		user = super(UserCreateForm, self).save(commit=False)
		user.mail = self.cleaned_data['email']
		if commit:
			user.save()
		return user

	def get_mensaje(self):
		return "Usuario " +  self.cleaned_data['first_name'] + " creado con exito, se detallan los permisos concedidos:"

	def get_permisos(self):
		return ('permiso1', 'permiso2',)



'''        
class RegistroUsuario(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombres','autofocus':'autofocus'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apellidos'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Contraseña','class':'form-control'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Contraseña','class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'email@email.com','class':'form-control'}))
'''      
