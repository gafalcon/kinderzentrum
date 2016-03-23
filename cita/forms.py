
from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
#from django.forms import ModelForm

# -*- coding: UTF8 -*-
class Ficha_DatosForm(forms.Form):
    
    Paciente = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'required': 'required'}),label="Paciente")

class Ficha_TerapiaForm(forms.Form):

    TIPOTERAPIACHOICES = (('1', 'Lenguaje'), ('2', 'Psicopedagogica'))
    TipoTerapia = forms.ChoiceField(widget = forms.Select(), choices= TIPOTERAPIACHOICES, required=True,  label='TipoTerapia')

class Ficha_TerapistaForm(forms.Form):

    TERAPISTACHOICES = (('1', 'Kerly Maldonado'), ('2', 'Silvia Sanchez'))
    Terapista = forms.ChoiceField(widget = forms.Select(), choices= TERAPISTACHOICES, required=True,  label='Terapista')


    