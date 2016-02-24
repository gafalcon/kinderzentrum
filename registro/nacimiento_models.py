# -*- coding: utf-8 -*-

from django.db import models

class Nacimiento(models.Model):
    nombre_lugar_nacimiento = models.CharField(max_length=500, blank=True)
    tipo_lugar_nacimiento = models.CharField(max_length=20)
    semana_gestacion = models.SmallIntegerField()
    tipo_nacimiento = models.CharField(max_length=100)
    tipo_inicio_parto = models.CharField(max_length=30)
    tipo_ruptura_agua = models.SmallIntegerField()
    sentimientos = models.CharField(max_length=500)
    duracion = models.SmallIntegerField()
    gemelar = models.BooleanField()
    primera_parte_cuerpo = models.SmallIntegerField()
    complicaciones = models.CharField(max_length=200)
    inyecciones = models.SmallIntegerField()
    complicaciones_cordon = models.SmallIntegerField()
