# -*- coding: utf-8 -*-
from asistencia.modelos.Tipo_terapia_model import Tipo_terapia
from django import forms
from django.forms import ModelForm
from django.forms import inlineformset_factory, BaseInlineFormSet, formset_factory, modelformset_factory
from django.forms.extras.widgets import SelectDateWidget
from modelos.cita_model import Cita
from registro.modelos.paciente_model import Paciente
#from django.core.exceptions import ValidationError
#import datetime

class CitaForm(ModelForm):
    # tipo_terapia = forms.ChoiceField(choices=Paciente.GRUPO_SANGUINEO_CHOICES,
    #                                     widget=forms.Select(attrs={'class':'form-control', 'required': 'required'}))
    error_css_class = 'has-error'
    
    class Meta:
        model = Cita
        fields =['hora_inicio',
                 'hora_fin',
                 'paciente',
                 'tipo_terapia'
                 ]        
       
        widgets = {'hora_inicio': forms.Select( attrs={'name':'start', 'id':'id_start','class':'form-control', 'required': 'required'}),
                   'hora_fin': forms.Select(attrs={'name':'end', 'id':'id_end','class':'form-control', 'required': 'required'}),
                   'paciente': forms.Select(attrs={'class':'form-control', 'required': 'required'}),
                   'tipo_terapia': forms.Select(attrs={'class':'form-control', 'required': 'required'}),
        }

        FIELD_NAME_MAPPING = {
                              'field1': 'start',
                              'field2': 'end'
                            }
        