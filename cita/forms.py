from django                                import forms
from django.forms                          import ModelForm
from django.forms                          import inlineformset_factory, BaseInlineFormSet, formset_factory, modelformset_factory
from django.forms.extras.widgets           import SelectDateWidget
from django.forms                          import inlineformset_factory, BaseInlineFormSet, formset_factory, modelformset_factory
from asistencia.modelos.Tipo_terapia_model import Tipo_terapia
from modelos.cita_model                    import Cita
from registro.modelos.paciente_model       import Paciente
