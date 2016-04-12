# -*- coding: utf-8 -*-
from django.db import models

class Tipo_terapia (models.Model):
    """ terapias recibidas por el paciente en kz"""
    costo = models.FloatField()
    nombre = models.CharField(max_length=200)
    tiempo = models.IntegerField()

    def __unicode__(self):
        return self.nombre
