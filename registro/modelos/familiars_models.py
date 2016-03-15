# -*- coding: utf-8 -*-

from django.db import models
#from .paciente_model  import Paciente

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

    parentezco = models.CharField(max_length=50)
    nombres = models.CharField(max_length=256)
    apellidos = models.CharField(max_length=256)
    nivel_estudio = models.CharField("nivel de estudio",
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
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.apellidos + " " + self.nombres


class DatosFamiliaresOtros(models.Model):
    "Datos de historia clinica familiar y otra informacion"

    numero_hermanos = models.PositiveSmallIntegerField()
    transtorno_hermanos = models.CharField(max_length=10)
    hermano_transtorno = models.PositiveSmallIntegerField()
    transtorno = models.CharField(max_length=10)
    alteracion_desarrollo = models.CharField(max_length=10)
    tipo_enfermedad_parientes = models.CharField(max_length=256)
    orientacion_a_institucion = models.CharField(max_length=100)

class Hermano(models.Model):
    "Datos de hermano"
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    datos_familiares = models.ForeignKey(DatosFamiliaresOtros, on_delete=models.CASCADE)
