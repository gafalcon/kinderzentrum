# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from modelos.historial_madre_models import HistorialMadre
from modelos.nacimiento_models import Nacimiento
from modelos.familiars_models import Familiar, Hermano, DatosFamiliaresOtros
from modelos.paciente_model import Paciente
from modelos.alimentacion_models import AlimentacionCostumbres, SuplementoAlimenticio
from modelos.primeros_dias_model import PrimerosDias
from modelos.recien_nacido_model import RecienNacido
from django.forms import inlineformset_factory, BaseInlineFormSet
import datetime

#from django.contrib.auth.models import User
CHOICES_SI_NO_DES = [(True,'Si'),(False,'No'), (None,'Desconoce')]

CHOICES_SI_NO = ((True, "Si"), (False, "No"))

class Ficha_PacienteForm(forms.Form):
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'required': 'required'}),label="Apellidos")
    nombres = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'required': 'required'}))
    nacimiento = forms.DateField( input_formats = ['%m/%d/%Y'],
                                  label='Fecha de nacimiento',
                                  widget=forms.TextInput(attrs=
                                                         {
                                                             'class':'datepicker form-control',
                                                             'required': 'required'
                                                         }))
    sexo = forms.ChoiceField(choices=Paciente.SEXO_CHOICES, widget=forms.RadioSelect(attrs={'required': 'required'}))    
    nacionalidad = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'required': 'required'}))
    lugar_nacimiento = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'required': 'required'}))
    grupo_sanguineo = forms.ChoiceField(choices=Paciente.GRUPO_SANGUINEO_CHOICES, widget=forms.Select(attrs={'class':'form-control', 'required': 'required'}))

class Ficha_DatosFamiliaresForm(forms.Form):
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nombres = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    parentesco = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nivel_estudio = forms.ChoiceField(choices=Familiar.NIVEL_ESTUDIO_CHOICES,
                                      widget=forms.Select(attrs={'class':'form-control'}),
                                      label='Nivel de estudio')
    #trabajo
    empresa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
                              label='Nombre de empresa',
                              required=False)
    direccion_empresa= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
                                       required=False,
                                       label='Dirección')
    jornada = forms.ChoiceField(choices=Familiar.JORNADA_TRABAJO_CHOICES,
                                widget=forms.Select(attrs={'class': 'form-control'}),
                                label='Jornada de Trabajo',
                                required=False)
    #domicilio
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
                                label='Dirección')
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
                               label='Teléfono')

class Ficha_DatosMedicoForm(forms.Form):
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nombres = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    area = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
   

class Ficha_DescripcionPacienteForm(forms.Form):
    CHOICES = [('papa','Papa'),('mama','Mama'),('abuelos','Abuelos'),('otros','Otros')]
    CHOICES_TERAPIA = [('rehabilitacion_fisica','Rehabilitacion Fisica'),('estimulacion_temprana','Estimulacion Temprana'),('ninguna','Ninguna')]
    CHOICES_DIFICULTADES = [('audicion','Audición'),('vision','Visión'),('lenguaje','Lenguaje'),('seguridad_si_mismo','Seguridad en sí mismo'),('comportamiento','Comportamiento'),('alimentacion','Alimentación'),('suenio','Sueño'),('interaccion_social','Interacción social'),('otro','Otro')]
    escripcion_pregunta_1 = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}), label="Que le preocupa de su hijo(a), algo especial que le llame la atencion?")
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
   
   

class NacimientoForm(ModelForm):
    gemelar = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="¿Fue embarazo gemelar?")
    medicamentos_parto = forms.ChoiceField(choices=CHOICES_SI_NO_DES, widget=forms.RadioSelect, label="¿Se le administró medicamentos o inyección durante el parto?")
    complicaciones_cordon = forms.ChoiceField(choices=CHOICES_SI_NO_DES, widget=forms.RadioSelect, label="¿Hubieron complicaciones en el cordón umbilical?")
    class Meta:
        model = Nacimiento
        fields = '__all__'
        widgets = {
            'tipo_lugar_nacimiento': forms.RadioSelect(choices=Nacimiento.TIPO_LUGAR_NACIMIENTO_CHOICES),
            'metodo_nacimiento': forms.CheckboxSelectMultiple(choices=Nacimiento.METODO_NACIMIENTO_CHOICES),
            'manera_inicio_parto': forms.RadioSelect(choices=Nacimiento.MANERA_INICIO_PARTO_CHOICES),
            'tipo_ruptura_fuente': forms.RadioSelect(choices=Nacimiento.TIPO_RUPTURA_FUENTE_CHOICES),
            'primera_parte_cuerpo': forms.RadioSelect(choices=Nacimiento.PRIMERA_PARTE_CUERPO_CHOICES),
            'complicaciones': forms.CheckboxSelectMultiple(choices=Nacimiento.COMPLICACIONES_CHOICES),
            'medicamentos_parto': forms.RadioSelect(choices=CHOICES_SI_NO_DES),
            'complicaciones_cordon': forms.RadioSelect(choices=CHOICES_SI_NO_DES),
        } 
    

class RecienNacidoForm(ModelForm):
    hubo_apego_precoz = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="¿Hubo apego precoz(le pusieron a su bebé encima del pecho cuando nació)?")
    permanecio_internado = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="¿Tuvo el bebé que permanecer internado cuando nació?")
    otra_complicacion = forms.CharField(required=False)
    class Meta:
        model = RecienNacido
        fields = ['edad_madre', 'edad_padre', 'peso', 'tamanio', 'diametro_encefalico', 'apgar_score', 'complicaciones_nacimiento', 'otra_complicacion', 'hubo_apego_precoz', 'tiempo_apego_precoz', 'tiempo_sostener_bebe','permanecio_internado', 'tiempo_internado', 'tipo_contacto', 'primera_lactancia'] 
        widgets = {
            'apgar_score': forms.RadioSelect(choices=RecienNacido.APGAR_CHOICES),
            'complicaciones_nacimiento': forms.CheckboxSelectMultiple(choices=RecienNacido.COMPLICACIONES_CHOICES),
            'tiempo_apego_precoz': forms.RadioSelect(choices=RecienNacido.APEGO_PRECOZ_CHOICES),
            'tiempo_sostener_bebe': forms.RadioSelect(choices=RecienNacido.SOSTENER_BEBE_CHOICES),
            'tipo_contacto': forms.RadioSelect(choices=RecienNacido.CONTACTO_CHOICES),
            'primera_lactancia': forms.RadioSelect(choices=RecienNacido.PRIMERA_LACTANCIA_CHOICES)
        }

    def clean(self):
        cleaned_data = super(RecienNacidoForm, self).clean()
        hubo_apego_precoz = cleaned_data.get('hubo_apego_precoz')
        permanecio_internado = cleaned_data.get('permanecio_internado')
        complicaciones = cleaned_data.get("complicaciones_nacimiento")
        if(hubo_apego_precoz == 'True'):
            tiempo =  cleaned_data.get('tiempo_apego_precoz')
            if not tiempo or tiempo == RecienNacido.APEGO_PRECOZ_NADA:
                self.add_error('tiempo_apego_precoz', "Debe llenar éste campo con valor distinto a Nada")
        if(permanecio_internado == 'True'):
            if not cleaned_data.get('tiempo_internado'):
                self.add_error('tiempo_internado', "Debe llenar éste campo")
            if not cleaned_data.get('tipo_contacto'):
                self.add_error('tipo_contacto', "Debe llenar éste campo")
        if(complicaciones and complicaciones.find("Otro") != -1):
            if not cleaned_data.get('otra_complicacion'):
                self.add_error('otra_complicacion', "Debe llenar éste campo")

    def save(self, complicaciones_list=None):
        model = super(RecienNacidoForm, self).save(commit=False)
        if self.cleaned_data.get('hubo_apego_precoz') == 'False':
            model.tiempo_apego_precoz = RecienNacido.APEGO_PRECOZ_NADA
        if self.cleaned_data.get('permanecio_internado') == 'False':
            model.tiempo_internado = datetime.timedelta()
            model.tipo_contacto = RecienNacido.CONTACTO_NINGUNA
        complicaciones = self.cleaned_data.get("complicaciones_nacimiento")
        if complicaciones and  complicaciones.find("Otro") != -1 and complicaciones_list:
            complicaciones_list.append(self.cleaned_data.get("otra_complicacion"))
        if complicaciones:
            model.complicaciones_nacimiento = ','.join(complicaciones_list)
        model.save()
        return model

class PrimerosDiasForm(ModelForm):
    clinica = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="¿El niño(a) tuvo que permanecer después de su nacimiento en una clínica u hospital?")
    dormia_toda_noche = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="¿El recién nacido dormía toda la noche?")
    otra_situacion = forms.CharField(required=False)
    otro_examen = forms.CharField(required=False)
    examenes = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=PrimerosDias.EXAMENES_CHOICES,
                                         label="¿Le realizaron al recién nacido algún tipo de exámen?",
                                         required=False)
    situaciones_despues_nacimiento = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=PrimerosDias.SITUACIONES_CHOICES,
                                         label="¿Presentó su bebé alguna de éstas situaciones después del nacimiento?",
                                         required=False)

    class Meta:
        model = PrimerosDias
        fields = ['clinica',
                  'clinica_permanencia',
                  'dias_permanencia',
                  'situaciones_despues_nacimiento',
                  'otra_situacion',
                  'icteria',
                  'tratamiento_icteria',
                  'examenes',
                  'otro_examen',
                  'dormia_toda_noche',
                  'veces_despertar_noche',
                  'lugar_dormir',
                  'descripcion_bebe',
                  'descripcion_madre'
        ]
        widgets = {
            'icteria': forms.RadioSelect(choices=CHOICES_SI_NO_DES),
            'situaciones_despues_nacimiento': forms.CheckboxSelectMultiple(choices=PrimerosDias.SITUACIONES_CHOICES),
            'lugar_dormir': forms.RadioSelect(choices=PrimerosDias.LUGAR_DORMIR_CHOICES)
        }
    def save(self):
        model = super(PrimerosDiasForm, self).save(commit=False)
        situaciones = self.cleaned_data.get('situaciones_despues_nacimiento')
        examenes = self.cleaned_data.get('examenes')
        if self.cleaned_data.get("clinica") == 'False':
            model.dias_permanencia = None
            model.clinica_permanencia = ''
        if not self.cleaned_data.get("icteria"):
            model.tratamiento_icteria = ''
        if self.cleaned_data.get('dormia_toda_noche') == 'True':
            model.veces_despertar_noche = 0
        if situaciones and "Otro" in situaciones:
            situaciones.append(self.cleaned_data.get('otra_situacion'))
        if examenes and "Otro" in examenes:
            examenes.append(self.cleaned_data.get('otro_examen'))
        if not examenes is None:
            model.examenes = ','.join(examenes)
        if not situaciones is None:
            model.situaciones_despues_nacimiento = ','.join(situaciones)
        model.save()
        return model

    def clean(self):
        cleaned_data = super(PrimerosDiasForm, self).clean()
        clinica = cleaned_data.get('clinica')
        dormia_toda_noche = cleaned_data.get('dormia_toda_noche')
        icteria = cleaned_data.get('icteria')
        situaciones = cleaned_data.get('situaciones_despues_nacimiento')
        examenes = cleaned_data.get('examenes')
        print("Examenes", examenes)
        print("situaciones", situaciones)
        if(icteria):
            if not cleaned_data.get('tratamiento_icteria'):
                self.add_error('tratamiento_icteria', "Debe llenar éste campo")
        if(clinica == 'True'):
            if not cleaned_data.get('clinica_permanencia'):
                self.add_error('clinica_permanencia', "Debe llenar éste campo")
            if not cleaned_data.get('dias_permanencia'):
                self.add_error('dias_permanencia', "Debe llenar éste campo")
        if(dormia_toda_noche == 'False'):
            veces = cleaned_data.get('veces_despertar_noche')
            if not veces or veces <= 0:
                self.add_error('veces_despertar_noche', "Debe llenar éste campo")
        if(situaciones and "Otro" in situaciones):
            if not cleaned_data.get('otra_situacion'):
                self.add_error('otra_situacion', "Debe llenar éste campo")
        if(examenes and "Otro" in examenes):
            if not cleaned_data.get('otro_examen'):
                self.add_error('otro_examen', "Debe llenar éste campo")


class AlimentacionForm(ModelForm):
    lactancia = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="¿Recibió lactancia materna?")
    motivo_suspencion_lactancia = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                            choices=AlimentacionCostumbres.MOTIVO_SUSPENSION_CHOICES,
                                                            label="¿Por qué suspendió la leche materna?", required=False)
    tiempo_leche_materna = forms.ChoiceField(widget= forms.RadioSelect,choices=AlimentacionCostumbres.TIEMPO_LACTANCIA_CHOICES,
                                             label="¿Cuánto tiempo recibió leche materna?", required=False)
    afecciones = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices = AlimentacionCostumbres.AFECCIONES_CHOICES,
                                           label="Indique si el niño ha tenido una de las siguientes afecciones",
                                           required=False)
    enfermedades = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices = AlimentacionCostumbres.ENFERMEDADES_CHOICES,
                                             label="¿Cuáles de las siguientes enfermedades ha presentado el niño(a)? Marque todas las que necesite",
                                             required=False)
    forma_alimento = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices = AlimentacionCostumbres.FORMA_ALIMENTO_CHOICES,
                                               label="¿Cuál era la forma o preparación del alimento?")
    apetito = forms.ChoiceField(widget=forms.RadioSelect, choices=AlimentacionCostumbres.APETITO_CHOICES, label="¿Cómo es el apetito del niño?")
    difiere_alimentacion = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="¿Difiere la alimentación del fin de semana de los demás días?")
    suplementos = forms.ChoiceField(choices=CHOICES_SI_NO, widget=forms.RadioSelect, label="¿Consumía suplementos alimenticios?")
    otro_motivo_suspencion_lactancia = forms.CharField(required=False)
    otra_afeccion = forms.CharField(required=False)
    otra_enfermedad = forms.CharField(required=False)
    otra_forma_alimento = forms.CharField(required=False)

    class Meta:
        model = AlimentacionCostumbres
        fields = '__all__'
        fields = ['lactancia','tiempo_leche_materna','motivo_suspencion_lactancia',
                  'otro_motivo_suspencion_lactancia','afecciones','otra_afeccion','enfermedades',
                  'otra_enfermedad','edad_alimentacion_complementaria','forma_alimento',
                  'otra_forma_alimento','lugar_desayuno','lugar_comida_media_manana',
                  'lugar_almuerzo','lugar_comida_media_tarde','lugar_cena','lugar_comida_otro',
                  'alimento_preferido','alimento_rechazado','suplementos','apetito',
                  'difiere_alimentacion','motivo_cambios_alimentacion'
        ]
    def clean(self):
        cleaned_data = super(AlimentacionForm, self).clean()
        lactancia = cleaned_data.get('lactancia')
        difiere_alimentacion = cleaned_data.get('difiere_alimentacion')
        motivo_suspencion_lactancia = cleaned_data.get('motivo_suspencion_lactancia')
        afecciones = cleaned_data.get('afecciones')
        enfermedades = cleaned_data.get('enfermedades')
        forma_alimento = cleaned_data.get('forma_alimento')
        if(lactancia == 'True'):
            if not cleaned_data.get('tiempo_leche_materna'):
                self.add_error('tiempo_leche_materna', "Debe llenar éste campo")
            if not cleaned_data.get('motivo_suspencion_lactancia'):
                self.add_error('motivo_suspencion_lactancia', "Debe llenar éste campo")
        if(difiere_alimentacion == 'True'):
            if not cleaned_data.get('motivo_cambios_alimentacion'):
                self.add_error('motivo_cambios_alimentacion', "Debe llenar éste campo")
        if motivo_suspencion_lactancia and "Otro" in motivo_suspencion_lactancia:
            if not cleaned_data.get('otro_motivo_suspencion_lactancia'):
                self.add_error('otro_motivo_suspencion_lactancia', "Debe llenar éste campo")
        if afecciones and "Otros" in afecciones:
            if not cleaned_data.get('otra_afeccion'):
                self.add_error('otra_afeccion', "Debe llenar éste campo")
        if enfermedades and "Otro" in enfermedades:
            if not cleaned_data.get('otra_enfermedad'):
                self.add_error('otra_enfermedad', "Debe llenar éste campo")
        if forma_alimento and "Otro" in forma_alimento:
            if not cleaned_data.get('otra_forma_alimento'):
                self.add_error("otra_forma_alimento", "Debe llenar éste campo")

    def save(self):
        model = super(AlimentacionForm, self).save(commit=False)
        motivo_suspencion_lactancia = self.cleaned_data.get('motivo_suspencion_lactancia')
        afecciones = self.cleaned_data.get('afecciones')
        enfermedades = self.cleaned_data.get('enfermedades')
        forma_alimento = self.cleaned_data.get('forma_alimento')
        if self.cleaned_data.get('lactancia') == 'False':
            model.tiempo_leche_materna = None
            model.motivo_suspencion_lactancia = None
            model.otro_motivo_suspencion_lactancia = ''
        elif motivo_suspencion_lactancia:
            model.motivo_suspencion_lactancia = ','.join(motivo_suspencion_lactancia)
        if self.cleaned_data.get('difiere_alimentacion') == 'False':
            model.motivo_cambios_alimentacion = ''
        if motivo_suspencion_lactancia and "Otro" in motivo_suspencion_lactancia:
            motivo_suspencion_lactancia.append(self.cleaned_data.get('otro_motivo_suspencion_lactancia'))
        if afecciones and "Otros" in afecciones:
            afecciones.append(self.cleaned_data.get('otra_afeccion'))
        if enfermedades and "Otro" in enfermedades:
            enfermedades.append(self.cleaned_data.get('otra_enfermedad'))
        if forma_alimento and "Otro" in forma_alimento:
            forma_alimento.append(self.cleaned_data.get('otra_forma_alimento'))
        if not afecciones is None:
            model.afecciones = ','.join(afecciones)
        if not enfermedades is None:
            model.enfermedades = ','.join(enfermedades)
        if forma_alimento:
            model.forma_alimento = ','.join(forma_alimento)
        model.save()
        return model


class DatosFamiliaresOtrosForm(ModelForm):

    orientacion_a_institucion = forms.ChoiceField(choices=DatosFamiliaresOtros.ORIENTACION_CHOICES,
                                                  widget=forms.RadioSelect, label="Quién los orientó a ésta institución?")
    otro_orientador = forms.CharField(required=False)
    class Meta:
        model = DatosFamiliaresOtros
        fields = '__all__'
        widgets = {
            'transtorno_hermanos': forms.RadioSelect(choices=CHOICES_SI_NO_DES),
            'alteracion_desarrollo': forms.RadioSelect(choices=CHOICES_SI_NO_DES)
        }
    def clean(self):
        cleaned_data = super(DatosFamiliaresOtrosForm, self).clean()
        numero_hermanos = cleaned_data.get('numero_hermanos')
        orientador =  cleaned_data.get('orientacion_a_institucion')
        if orientador and orientador == DatosFamiliaresOtros.ORIENTACION_OTRO:
            if not cleaned_data.get('otro_orientador'):
                self.add_error('otro_orientador', "Debe llenar éste campo")
        if numero_hermanos > 0:
            trans_hermanos = cleaned_data.get('transtorno_hermanos')
            if trans_hermanos:
                hermano_transtorno = cleaned_data.get("hermano_transtorno")
                if not hermano_transtorno:
                    self.add_error('hermano_transtorno', "Debe llenar éste campo")
                elif hermano_transtorno > numero_hermanos or hermano_transtorno <= 0:
                    self.add_error('hermano_transtorno', "No tiene tantos hermanos")
                if not cleaned_data.get('transtorno'):
                    self.add_error('transtorno', "Debe llenar éste campo")

    def save(self):
        model = super(DatosFamiliaresOtrosForm, self).save(commit=False)
        orientador = self.cleaned_data.get('orientacion_a_institucion')
        numero_hermanos = self.cleaned_data.get('numero_hermanos')
        if orientador == DatosFamiliaresOtros.ORIENTACION_OTRO:
            model.orientacion_a_institucion = self.cleaned_data.get('otro_orientador')
        if numero_hermanos <= 0:
            model.transtorno_hermanos = None
            model.hermano_transtorno = 0
            model.transtorno = ''
        model.save()
        return model

       
class SuplementoFormset(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(SuplementoFormset, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

SuplementosFormset = inlineformset_factory(AlimentacionCostumbres, SuplementoAlimenticio,
                                           formset=SuplementoFormset,
                                           fields='__all__',
                                           can_delete=False,
                                           extra=1
)

class HermanoFormset(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(HermanoFormset, self).__init__(*args, **kwargs) 
        for form in self.forms:
            form.empty_permitted = False


class HermanoForm(ModelForm):
    fecha_nacimiento = forms.DateField(input_formats=['%m/%d/%Y'],
                                       label='Fecha de nacimiento',
                                       widget=forms.TextInput(attrs={'class':'datepicker form-control'}))
    class Meta:
        model = Hermano
        fields = '__all__'

HermanosFormset = inlineformset_factory(DatosFamiliaresOtros, Hermano,
                                        fields='__all__',
                                        form=HermanoForm,
                                        formset=HermanoFormset,
                                        can_delete=False)
                                        # widgets={'fecha_nacimiento': forms.TextInput(attrs={'class':'datepicker form-control'}),
                                        #          'nombres': forms.TextInput(attrs={'class': 'form-control'}),
                                        #          'apellidos': forms.TextInput(attrs={'class': 'form-control'})
                                        # }
 





