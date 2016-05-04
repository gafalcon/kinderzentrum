# -*- coding: utf-8 -*-
import datetime
from django.db                             import models
from asistencia.modelos.Tipo_terapia_model import Tipo_terapia
from asistencia.modelos.Terapista_model    import Terapista
from registro.modelos.paciente_model       import Paciente


class Cita(models.Model):
    """ Representa la cita del paciente """
    ESTADO_CHOICES = (
        ("A", "Agendada"),
        ("S", "Asistio"),
        ("N", "No asistio"),
        ("C", "Cancelada")
    )    
    fecha_registro = models.DateField(auto_now_add = True)
    #fecha_registro= models.DateField(default=datetime.date.today)
    fecha_cita     = models.DateField(auto_now_add = False)    
    hora_inicio    = models.TimeField(auto_now = False)
    hora_fin       = models.TimeField(auto_now = False)
    #hora_inicio   = models.TimeField(default = datetime.datetime.now().time() )
    estado         = models.CharField(choices=ESTADO_CHOICES, max_length=2, default='A')
    indicaciones   = models.CharField(max_length=256)  
    tipo_terapia   = models.ForeignKey(Tipo_terapia, on_delete=models.CASCADE)
    paciente       = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    terapista      = models.ForeignKey(Terapista, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.indicaciones
    #def __unicode__(self):
        #return str(self.paciente)
    #python 3.3 is def __str__(self):