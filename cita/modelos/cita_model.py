# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from registro.modelos.descripcion_models import* #import Terapia, Medicamento
from registro.modelos.terapista_model import Terapista
from registro.modelos.paciente_model import Paciente


class Cita(models.Model):
    """ Representa la cita del paciente """
    fecha_registro = models.DateTimeField( auto_now = True )
    fecha_cita = models.DateTimeField( auto_now = True )
    hora_inicio = models.CharField(max_length=8)
    hora_fin = models.CharField(max_length=8)
    cancelo_cita = models.CharField(max_length=1)
    asistio_cita = models.CharField(max_length=1)
    valor_sesion = models.PositiveIntegerField()
    terapia_id = models.OneToOneField(Terapia)
    terapista_id = models.ForeignKey(Terapista, on_delete=models.CASCADE)
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medicamento_id = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    indicaciones = models.CharField(max_length=256)
    examenes = models.CharField(max_length=256)
    


    def __unicode__(self):
        return self.paciente_id

class Cita_Medicamento(models.Model):
    """ Relación entre Cita y Medicamento """
    
    cita = models.ForeignKey(Cita)
    medicamento = models.ForeignKey(Medicamento)
    prescripcion = models.CharField(max_length=256)
