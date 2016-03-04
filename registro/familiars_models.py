# -*- coding: utf-8 -*-

from django.db import models

class Familiar(models.Model):
    """ Familiar del paciente """
    
    ESTUDIO_PRIMARIA = 0
    ESTUDIO_SECUNDARIA = 1
    ESTUDIO_SUPERIOR = 2
    NIVEL_ESTUDIO_CHOICES = (
        (ESTUDIO_PRIMARIA, "Primaria"),
        (ESTUDIO_SECUNDARIA, "Secundaria"),
        (ESTUDIO_SUPERIOR, "Superior")
    )

    TRABAJO_TIEMPO_COMPLETO = 0
    TRABAJO_MEDIO_TIEMPO = 1 
    TRABAJO_POR_HORAS = 2
    JORNADA_TRABAJO_CHOICES = (
        (TRABAJO_TIEMPO_COMPLETO, "Tiempo completo"),
        (TRABAJO_MEDIO_TIEMPO, "Medio tiempo"),
        (TRABAJO_POR_HORAS, "Por horas")
    )

    tipo = models.CharField(max_length=50, default='madre')
    nombres = models.CharField(max_length=256)
    apellidos = models.CharField(max_length=256)
    nivel_studio = models.CharField("nivel de estudio",
                                    choices=NIVEL_ESTUDIO_CHOICES,
                                    max_length=20)
    direccion = models.CharField("dirección", max_length=256)
    telefonos = models.CharField("teléfono", max_length=50)
    empresa = models.CharField("lugar de trabajo",
                               max_length=256,
                               blank=True)
    direccion_empresa = models.CharField("dirección de empresa",
                                         max_length=256,
                                         blank=True)
    jornada = models.PositiveSmallIntegerField("jornada de trabajo", choices = JORNADA_TRABAJO_CHOICES)

    def __unicode__(self):
        return self.apellidos + " " + self.nombres

