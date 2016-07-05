# -*- encoding: utf-8 -*-
import datetime
from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django.forms import inlineformset_factory, BaseInlineFormSet, formset_factory, modelformset_factory
from modelos.cita_model import Cita


HORARIO_CHOICES = (
        ("08:00", "08:00"),
        ("08:30", "08:30"),
        ("09:00", "09:00"),
        ("09:30", "09:30"),
        ("10:00", "10:00"),
        ("10:30", "10:30"),
        ("11:00", "11:00"), 
        ("11:30", "11:30"),   
        ("12:00", "12:00"),
        ("12:30", "12:30"),
        ("13:00", "13:00"),
        ("13:30", "13:30"),
        ("14:00", "14:00"),
        ("14:30", "14:30"),
        ("15:00", "15:00"), 
        ("15:30", "15:30"),   
        ("16:00", "16:00"),
        ("16:30", "16:30"),
        ("17:00", "17:00"),
        ("17:30", "17:30"),
        ("18:00", "18:00"),
        ("18:30", "18:30"),
        ("19:00", "19:00")            
    )

DATEFORMAT = '%d/%m/%Y'

class CitaForm(ModelForm):
    # grupo_sanguineo = forms.ChoiceField(choices=Paciente.GRUPO_SANGUINEO_CHOICES,
    #                                     widget=forms.Select(attrs={'class':'form-control', 'required': 'required'}))
    error_css_class = 'has-error'
    fecha_cita = forms.DateField(input_formats=[DATEFORMAT],
                                       label='Fecha de cita',
                                       widget=forms.DateInput(attrs=
                                                              {
                                                                  'class':'datepicker form-control',
                                                                  'required': 'required'
                                                              },
                                                              format=DATEFORMAT))
    class Meta:
        model = Cita
        fields = ['fecha_cita',
                  'hora_inicio',
                  'hora_fin',
                  'estado',
                  'indicaciones',
                  'tipo_terapia',
                  'paciente',
                  'terapista']
        widgets = {'hora_inicio': forms.Select(choices=HORARIO_CHOICES,  attrs={'class':'form-control', 'required': 'required'}),
                   'hora_fin': forms.Select(choices=HORARIO_CHOICES,  attrs={'class':'form-control', 'required': 'required'})
        }