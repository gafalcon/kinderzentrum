# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.db import models
from registro.modelos.descripcion_models import* #import Terapia, Medicamento, Terapista
#from registro.modelos.terapista_model import *
from registro.modelos.paciente_model import Paciente


class Cita(models.Model):
    """ Representa la cita del paciente """
    fecha_registro = models.DateTimeField( auto_now = True )
    fecha_cita = models.DateTimeField( auto_now = True )
    hora_inicio = models.TimeField(auto_now=False)
    hora_fin = models.TimeField(auto_now=False)
    cancelo_cita = models.BooleanField()
    asistio_cita = models.CharField(max_length=1)
    indicaciones = models.CharField(max_length=256)  
    terapista_id = models.ForeignKey(Terapista, on_delete=models.CASCADE)
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)    


    def __unicode__(self):
        return self.paciente_id





