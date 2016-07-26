# -*- encoding: utf-8 -*-
from django                                 import forms
from modelos.Terapista_model                import Terapista
from modelos.Tipo_terapia_model             import Tipo_terapia

class ConsultaAsistenciaForm (forms.Form):
    nombre = forms.CharField()

class TerapistaForm(ModelForm):
    required_css_class = 'required'
    #error_css_class = 'has-error'
    
    class Meta:
        model = Terapista
        fields = ['cedula',
                  'nombres',
                  'apellidos',                                    
                  'direccion',
                  'telefonos',
                  'fecha_nacimiento'
                  ]                         

class Tipo_terapiaForm(ModelForm):
    required_css_class = 'required'
    #error_css_class = 'has-error'
    
    class Meta:
        model = Tipo_terapia
        fields = ['costo',
                  'nombre',
                  'tiempo'
                  ]     