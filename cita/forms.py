# -*- encoding: utf-8 -*-
import datetime
from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminTimeWidget
from django.forms.extras.widgets import SelectDateWidget
from django.forms import inlineformset_factory, BaseInlineFormSet, formset_factory, modelformset_factory
from modelos.cita_model import Cita

DATEFORMAT = '%d/%m/%Y'

class CitaForm(ModelForm):
    error_css_class = 'has-error'
    fecha_cita = forms.DateField(input_formats=[DATEFORMAT],
                                       label='Fecha de cita',
                                       widget=forms.DateInput(attrs=
                                                              {
                                                                  'class':'datepicker form-control',
                                                                  'required': 'required'
                                                              },
                                                              format=DATEFORMAT))
    hora_inicio = forms.TimeField(widget=AdminTimeWidget(format='%H:%M'))
    hora_fin    = forms.TimeField(widget=AdminTimeWidget(format='%H:%M'))

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