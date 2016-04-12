# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from modelos.cita_model import Cita
from asistencia.modelos.Tipo_terapia_model import Tipo_terapia
from registro.modelos.paciente_model import Paciente
from django.forms.extras.widgets import SelectDateWidget
from django.forms import inlineformset_factory, BaseInlineFormSet, formset_factory, modelformset_factory

#from django.core.exceptions import ValidationError
#import datetime

class CitaForm(ModelForm):
    # tipo_terapia = forms.ChoiceField(choices=Paciente.GRUPO_SANGUINEO_CHOICES,
    #                                     widget=forms.Select(attrs={'class':'form-control', 'required': 'required'}))
    error_css_class = 'has-error'
    
    class Meta:
        model = Cita
        fields =['paciente',
                 'tipo_terapia'
                 ]        
        #widgets = {'tipo_terapia': forms.ModelChoiceField(queryset=Tipo_terapia.objects.all().order_by('nombre'))}
        #widgets = {'tipo_terapia': forms.ModelChoiceField(queryset=Tipo_terapia.objects.all())}
        widgets = {'paciente': forms.Select(attrs={'class':'form-control', 'required': 'required'}),
                   'tipo_terapia': forms.Select(attrs={'class':'form-control', 'required': 'required'}),
        }