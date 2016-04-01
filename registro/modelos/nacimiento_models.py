# -*- coding: utf-8 -*-

from django.db import models

class Nacimiento(models.Model):
    nombre_lugar_nacimiento = models.CharField(max_length=500, blank=True)
    tipo_lugar_nacimiento = models.CharField(max_length=20)
    semana_gestacion = models.PositiveSmallIntegerField()
    metodo_nacimiento = models.CharField(max_length=100)
    manera_inicio_parto = models.CharField(max_length=30)
    tipo_ruptura_fuente= models.CharField(max_length=100)
    sentimientos_parto = models.CharField(max_length=500)
    sentimientos_nacimiento = models.CharField(max_length=500)
    duracion_nacimiento = models.PositiveSmallIntegerField()
    gemelar = models.BooleanField()
    primera_parte_cuerpo = models.CharField(max_length=50)
    complicaciones = models.CharField(max_length=200)
    complicaciones_cordon = models.CharField(max_length=10)
    #medicamentos_parto = models.Field(max_length=10)
