# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from modelos.historial_madre_models import HistorialMadre
from modelos.familiars_models import Familiar, Hermano, DatosFamiliaresOtros
from modelos.paciente_model import Paciente
from modelos.alimentacion_models import AlimentacionCostumbres
from django.forms import inlineformset_factory
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
    CHOICES_DIFICULTADES = [('audicion','Audición'),('vision','Visión'),('lenguaje','Lenguaje'),('seguridad_si_mismo','Seguridad en sí mismo'),('comportamiento','Comportamiento'),('alimentacion','Alimentación'),('suenio','Sueño'),('interaccion_social','Interacción social'),('otro','Otro')]
    CHOICES_SI_NO_DES = [('desconoce','Desconoce'),('si','Si'),('no','No')]
    descripcion_pregunta_1 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}), label="Que le preocupa de su hijo(a), algo especial que le llame la atencion?")
    descripcion_pregunta_2 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'form-control'}), label="Quien descubrio estas molestias?")
    descripcion_otros_2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','oculto':'oculto'}), initial='Especifique')
    descripcion_pregunta_3 = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="Se encuentra en algun tratamiento?")
    descripcion_pregunta_4 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'3','oculto':'oculto'}), label="En donde realiza el tratamiento?")
    descripcion_pregunta_5 = forms.MultipleChoiceField(required=True,choices=CHOICES_TERAPIA, widget=forms.CheckboxSelectMultiple, label="Que tipo de terapia realiza?")
    descripcion_tiempo_rehab_fisica =  forms.CharField(label="Tiempo en terapia de rehabilitacion fisica?", widget=forms.TextInput(attrs={'class':'form-control','oculto':'oculto'}), initial='Especifique tiempo')
    descripcion_tiempo_estimu_temprana = forms.CharField(label="Tiempo en terapia de estimulacion temprana?", widget=forms.TextInput(attrs={'class':'form-control','oculto':'oculto'}), initial='Especifique tiempo')
    descripcion_pregunta_6 = forms.MultipleChoiceField(required=True,choices=CHOICES_DIFICULTADES, widget=forms.CheckboxSelectMultiple, label="Ha presentado su hijo(a) algun tipo de dificultades en estas aereas? marque todas las opciones que desee.")
    descripcion_otros_6 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','oculto':'oculto'}), initial='Especifique',label="Especifique otros")
    descripcion_pregunta_7 = forms.ChoiceField(choices=CHOICES_SI_NO_DES, widget=forms.Select(attrs={'class':'form-control'}), label="Existe alguna limitacion con sus movimientos?")
    descripcion_pregunta_8 = forms.ChoiceField(choices=CHOICES_SI_NO_DES, widget=forms.Select(attrs={'class':'form-control'}), label="Ha tenido convulsiones?")
    descripcion_pregunta_8_1 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'2','oculto':'oculto'}), label="Que tipo de crisis tuvo durante la convulsion?")
    descripcion_pregunta_8_2 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'1','oculto':'oculto'}), label="A que edad fue la primera crisis?")
    descripcion_pregunta_8_3 = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.Select(attrs={'class':'form-control','oculto':'oculto'}), label="Tomo medicamentos?")
    descripcion_pregunta_8_4 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'2','oculto':'oculto'}), label="Que medicamentos y dosis diaria tomo?")
    

class Ficha_HistorialMadreForm(forms.Form):
    CHOICES_ENFERMEDADES = [('diabetes','Diabetes'),('hipertension','Hipertension'),('infeccion_urinaria','Infecciones en las vias urinarias'),('ninguna_enf','Ninguna')]
    CHOICES_ENFERMEDADES_ANTES_EMBARA = [('enfer_cardiacas','Enfermedades cardiacas'),('enfer_hepaticas','Enfermedades hepaticas'),('enfer_mentales','Enfermedades mentales'),('proble_azucar','Problemas con el azucar'),('ninguna','Ninguna'),('otro','Otros')]
    CHOICES_SI_NO = [('si','Si'),('no','No')]
    CHOICES_ANTICONCEPTIVO = [('pildoras','Pildoras'),('ritmo','Ritmo'),('diu_cobre','Diu de cobre'),('preservativos','Preservativos'),('parches','Parches'),('anillo_vaginal','Anillo vaginal'),('implante_sudermico','Implante sudermico'),('inyectables','Inyectables')]
    pregunta_5_1 = forms.MultipleChoiceField(required=True, choices=CHOICES_ENFERMEDADES, widget=forms.CheckboxSelectMultiple, label="Indique si durante el embarazo sufrio algunas de las siguientes enfermedades?")
    otros_5_1_1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','oculto':'oculto'}), initial='Especifique',label="Especifique otros")
    pregunta_5_2 = forms.MultipleChoiceField(required=True, choices=CHOICES_ENFERMEDADES_ANTES_EMBARA, widget=forms.CheckboxSelectMultiple, label="Indique si durante el embarazo sufrio algunas de las siguientes enfermedades?")
    otros_5_2_1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','oculto':'oculto'}), initial='Especifique',label="Especifique otros")
    pregunta_5_3 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'2'}), label="Indique algun tipo de enfermedad cronica")
    pregunta_5_4 = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="Tuvo usted alguna defuncion fetal antes de concebir al bebe/ninio(a) que trae a consulta?")
    otros_5_4_1 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','oculto':'oculto'}), initial='Especifique',label="Cuantas defunciones fetales a tenido durante su vida:")
    pregunta_5_5 = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="Ha tenido hijos muertos?")
    otros_5_5_1 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','oculto':'oculto'}), label="Numero de hijos nacidos muertos:")
    otros_5_5_2 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','oculto':'oculto'}), label="Numero de hijos nacidos vivos:")
    pregunta_5_6 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label="Numero de embarazos:")
    pregunta_5_7 = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="Utilizo algun metodo anticonceptivo antes de estar embarazada?")
    otros_5_7_1 = forms.MultipleChoiceField(required=True, choices=CHOICES_ANTICONCEPTIVO, widget=forms.CheckboxSelectMultiple(attrs={'oculto':'oculto'}))
    pregunta_5_8 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}), label="Tuvo usted alguna enfermedad grave, dolencia, accidente o infeccion, antes de concebir a este bebe? (ejemplo: cistitis, dolor pelvico, menstruaciones dolorosas, migranias, etc.)")
   
   

'''
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
'''


class AlimentacionForm(ModelForm):
    CHOICES_SI_NO = [('si','Si'),('no','No')]
    lactancia = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="¿Recibió lactancia materna?")
    motivo_suspencion_lactancia = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                            choices=AlimentacionCostumbres.MOTIVO_SUSPENSION_CHOICES,
                                                            label="¿Por qué suspendió la leche materna?")
    tiempo_leche_materna = forms.ChoiceField(widget= forms.RadioSelect,choices=AlimentacionCostumbres.TIEMPO_LACTANCIA_CHOICES,
                                             label="¿Cuánto tiempo recibió leche materna?")
    afecciones = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices = AlimentacionCostumbres.AFECCIONES_CHOICES,
                                           label="Indique si el niño ha tenido una de las siguientes afecciones")
    enfermedades = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices = AlimentacionCostumbres.ENFERMEDADES_CHOICES,
                                           label="¿Cuáles de las siguientes enfermedades ha presentado el niño(a)? Marque todas las que necesite")

    forma_alimento = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices = AlimentacionCostumbres.FORMA_ALIMENTO_CHOICES,
                                               label="¿Cuál era la forma o preparación del alimento?")

    apetito = forms.ChoiceField(widget=forms.RadioSelect, choices=AlimentacionCostumbres.APETITO_CHOICES, label="¿Cómo es el apetito del niño?")

    difiere_alimentacion = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="¿Difiere la alimentación del fin de semana de los demás días?")
    suplementos = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="¿Consumía suplementos alimenticios?")

    class Meta:
        model = AlimentacionCostumbres
        fields = '__all__'
        fields = ['lactancia',
                  'tiempo_leche_materna',
                  'motivo_suspencion_lactancia',
                  'afecciones',
                  'enfermedades',
                  'edad_alimentacion_complementaria',
                  'forma_alimento',
                  'lugar_desayuno',
                  'lugar_comida_media_manana',
                  'lugar_almuerzo',
                  'lugar_comida_media_tarde',
                  'lugar_cena',
                  'lugar_comida_otro',
                  'alimento_preferido',
                  'alimento_rechazado',
                  'suplementos',
                  'apetito',
                  'difiere_alimentacion',
                  'motivo_cambios_alimentacion'
        ]
        # widgets = {
        #      'tiempo_leche_materna': forms.RadioSelect
        #  }

class DatosFamiliaresOtrosForm(ModelForm):

    orientacion_a_institucion = forms.ChoiceField(choices=DatosFamiliaresOtros.ORIENTACION_CHOICES,
                                                  widget=forms.RadioSelect, label="Quién los orientó a ésta institución?")
    class Meta:
        CHOICES_SI_NO_DES = [(2,'Si'),(3,'No'), (1,'Desconoce')]
        model = DatosFamiliaresOtros
        fields = '__all__'
        widgets = {
            'transtorno_hermanos': forms.RadioSelect(choices=CHOICES_SI_NO_DES),
            'alteracion_desarrollo': forms.RadioSelect(choices=CHOICES_SI_NO_DES)
        }
        


HermanosFormset = inlineformset_factory(DatosFamiliaresOtros, Hermano,
                                        fields='__all__',
                                        can_delete=False,
                                        widgets={'fecha_nacimiento': forms.TextInput(attrs={'class':'datepicker form-control'}),
                                                 'nombres': forms.TextInput(attrs={'class': 'form-control'}),
                                                 'apellidos': forms.TextInput(attrs={'class': 'form-control'})
                                        }
) 
