# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
#from django.core.exceptions import ValidationError
#import datetime

# def validate_current_century(value):
#     if value < 2000 or value > 2050:
#         raise ValidationError(u'%s is not a valid year!' % value)

class Ficha_DatosForm(forms.Form):
    TIPOTERAPIACHOICES = ((1, "REHABILITACIÓN FÍSICA"),
                          (2, "ESTIMULACIÓN TEMPRANA"),
                          (3, "INTEGRACIÓN SENSORIAL"),
                          (4, "HIPOTERAPIA"),
                          (5, "LENGUAJE"),
                          (6, "PSICOPEDAGÓGICA"),
                          (7, "TERAPIA FAMILIAR"),
                          (8, "NINGUNA"))
    TERAPISTACHOICES = (('1', 'Kerly Maldonado'), 
                        ('2', 'Silvia Sánchez'))
    HORARIOCHOICES = (('08:00 - 09:00', '08:00 - 09:00'),
                      ('09:00 - 10:00', '09:00 - 10:00'),
                      ('10:00 - 11:00', '10:00 - 11:00'),
                      ('11:00 - 12:00', '11:00 - 12:00'),
                      ('12:00 - 13:00', '12:00 - 13:00'),
                      ('13:00 - 14:00', '13:00 - 14:00'),
                      ('14:00 - 15:00', '14:00 - 15:00'),
                      ('15:00 - 16:00', '15:00 - 16:00'),
                      ('16:00 - 17:00', '16:00 - 17:00'),
                      ('17:00 - 18:00', '17:00 - 18:00'),
                      ('18:00 - 19:00', '18:00 - 19:00')
                      )
    #Paciente = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'autocomplete':'on', 'required': 'required'}),label="Paciente")
    Paciente = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'autocomplete':'on', 'required': 'required'}),label="Paciente")
    TipoTerapia = forms.ChoiceField(choices=TIPOTERAPIACHOICES, widget=forms.Select(attrs={'class':'form-control', 'required': 'required'}), 
                                 label='Tipo de terapia')
    Terapista = forms.ChoiceField(choices=TERAPISTACHOICES, widget=forms.Select(attrs={'class':'form-control', 'required': 'required'}), label='Terapista')
    fecha_cita = forms.DateField( input_formats = ['%m/%d/%Y'],
                                  widget=forms.TextInput(attrs=
                                                         {
                                                             'class':'datepicker2',
                                                             'required': 'required'
                                                         }))
    Horario = forms.ChoiceField(choices=HORARIOCHOICES, widget=forms.Select(attrs={'class':'form-control', 'required': 'required'}))


class Ficha_ConsCitaTerapistaForm(forms.Form):

    TERAPISTACHOICES = (('1', 'Kerly Maldonado'), 
                        ('2', 'Silvia Sánchez'))
    Terapista  = forms.ChoiceField(choices=TERAPISTACHOICES, widget=forms.Select(attrs={'class':'form-control', 'required': 'required'}), label='Terapista')
    fecha_cita_inicio = forms.DateField(  input_formats = ['%d/%m/%Y'],
                                          label = "Fecha inicial",
                                          widget=forms.TextInput(attrs=
                                          {
                                            'class':'datepicker2',
                                            'required': 'required'
                                          }))
    fecha_cita_fin = forms.DateField( input_formats = ['%d/%m/%Y'],
                                      label = "Fecha final",
                                      widget=forms.TextInput(attrs=
                                      {
                                        'class':'datepicker2',
                                        'required': 'required'
                                      }))