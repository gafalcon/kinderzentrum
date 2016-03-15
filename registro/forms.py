# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from modelos.historial_madre_models import HistorialMadre
from modelos.familiars_models import Familiar
from modelos.paciente_model import Paciente
import datetime
#from django.contrib.auth.models import User



class Ficha_PacienteForm(forms.Form):
    SEXO=[('masculino','Masculino'),('femenino','Femenino')]
    GRUPO_SANGUINEO = [('o+','O+'),('o-','O-'),('a+','A+'),('a-','A-'),('b+','B+'),('b-','B-'),('ab+','AB+'),('ab-','AB-')]
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Apellidos")
    nombres = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nacimiento = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker form-control'
                                }))
    sexo = forms.ChoiceField(choices=SEXO, widget=forms.RadioSelect())    
    nacionalidad = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    lugar_nacimiento = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    grupo_sanguineo = forms.ChoiceField(choices=GRUPO_SANGUINEO, widget=forms.Select(attrs={'class':'form-control'}))

class Ficha_DatosFamiliaresForm(forms.Form):
    ESTUDIO=[('primaria','Primaria'),('secundaria','Secundaria'),('universitaria','Universitaria'),('superior','Superior')]
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nombres = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    parentesco = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nivel_estudio = forms.ChoiceField(choices=ESTUDIO, widget=forms.Select(attrs={'class':'form-control'}))
    #trabajo
    empresa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    empresa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    #domicilio
    direccion_domicilio = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class Ficha_DatosMedicoForm(forms.Form):
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nombres = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    area = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
   

class Ficha_DescripcionPacienteForm(forms.Form):
    CHOICES = [('papa','Papa'),('mama','Mama'),('abuelos','Abuelos'),('otros','Otros')]
    CHOICES_SI_NO = [('si','Si'),('no','No')]
    CHOICES_TERAPIA = [('rehabilitacion_fisica','Rehabilitacion Fisica'),('estimulacion_temprana','Estimulacion Temprana'),('ninguna','Ninguna')]
    CHOICES_DIFICULTADES = [('audicion','Audicion'),('vision','Vision'),('lenguaje','Lenguaje'),('seguridad_si_mismo','Seguridad en si mismo'),('comportamiento','Comportamiento'),('alimentacion','Alimentacion'),('suenio','Suenio'),('interaccion_social','Interacion social'),('otro','Otro')]
    CHOICES_SI_NO_DES = [('desconoce','Desconoce'),('si','Si'),('no','No')]
    descripcion_pregunta_1 = forms.CharField(widget=forms.Textarea(attrs={'rows':'3'}), label="Que le preocupa de su hijo(a), algo especial que le llame la atencion?")
    descripcion_pregunta_2 = forms.ChoiceField(choices=CHOICES, widget=forms.Select, label="Quien descubrio estas molestias?")
    descripcion_otros_2 = forms.CharField(widget=forms.TextInput(attrs={'oculto':'oculto'}), initial='Especifique')
    descripcion_pregunta_3 = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="Se encuentra en algun tratamiento?")
    descripcion_pregunta_4 = forms.CharField(widget=forms.Textarea(attrs={'rows':'3','oculto':'oculto'}), label="En donde realiza el tratamiento?")
    descripcion_pregunta_5 = forms.MultipleChoiceField(required=True,choices=CHOICES_TERAPIA, widget=forms.CheckboxSelectMultiple, label="Que tipo de terapia realiza?")
    descripcion_tiempo_rehab_fisica =  forms.CharField(label="Tiempo en terapia de rehabilitacion fisica?", widget=forms.TextInput(attrs={'oculto':'oculto'}), initial='Especifique tiempo')
    descripcion_tiempo_estimu_temprana = forms.CharField(label="Tiempo en terapia de estimulacion temprana?", widget=forms.TextInput(attrs={'oculto':'oculto'}), initial='Especifique tiempo')
    descripcion_pregunta_6 = forms.MultipleChoiceField(required=True,choices=CHOICES_DIFICULTADES, widget=forms.CheckboxSelectMultiple, label="Ha presentado su hijo(a) algun tipo de dificultades en estas aereas? marque todas las opciones que desee.")
    descripcion_otros_6 = forms.CharField(widget=forms.TextInput(attrs={'oculto':'oculto'}), initial='Especifique',label="Especifique otros")
    descripcion_pregunta_7 = forms.ChoiceField(choices=CHOICES_SI_NO_DES, widget=forms.Select, label="Existe alguna limitacion con sus movimientos?")
    descripcion_pregunta_8 = forms.ChoiceField(choices=CHOICES_SI_NO_DES, widget=forms.Select, label="Ha tenido convulsiones?")
    descripcion_pregunta_8_1 = forms.CharField(widget=forms.Textarea(attrs={'rows':'2','oculto':'oculto'}), label="Que tipo de crisis tuvo durante la convulsion?")
    descripcion_pregunta_8_2 = forms.CharField(widget=forms.Textarea(attrs={'rows':'1','oculto':'oculto'}), label="A que edad fue la primera crisis?")
    descripcion_pregunta_8_3 = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.Select(attrs={'oculto':'oculto'}), label="Tomo medicamentos?")
    descripcion_pregunta_8_4 = forms.CharField(widget=forms.Textarea(attrs={'rows':'2','oculto':'oculto'}), label="Que medicamentos y dosis diaria tomo?")
    

class Ficha_HistorialMadreForm(forms.Form):
    
        

class HistorialMadreForm(ModelForm):
    class Meta:
        model = HistorialMadre
        fields = ['defunciones_fetales', 'hijos_nacidos_muertos', 
                  'hijos_nacidos_vivos', 'enfermedades_previas',
                  'anticonceptivos']




class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        exclude = ['descripcion', 'historial_madre', 'gestacion', 'nacimiento', 'medico']

class MadreForm(ModelForm):
    class Meta:
        model = Familiar
        fields = '__all__'

class PadreForm(ModelForm):
    class Meta:
        model = Familiar
        fields = '__all__'
        #exclude = ['tipo']
