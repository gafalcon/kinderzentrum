# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
import descripcion_models
import historial_madre_models
import nacimiento_models

class Familiar(models.Model):
    """ Familiar del paciente """
    NIVEL_ESTUDIO_CHOICES = (
        ("Superior", "Superior"),
        ("Bachiller", "Bachiller")
    )
    nombres = models.CharField(max_length=256)
    apellidos = models.CharField(max_length=256)
    nivel_studio = models.CharField("Nivel de Studio",
                                    choices=NIVEL_ESTUDIO_CHOICES,
                                    max_length=20)
    direccion = models.CharField(max_length=256)
    telefonos = models.CharField(max_length=50)
    empresa = models.CharField("lugar de trabajo",
                               max_length=256,
                               blank=True)
    direccion_empresa = models.CharField("direccion de empresa",
                                         max_length=256,
                                         blank=True)
    jornada = models.CharField("jornada de trabajo", max_length=50)

    def __unicode__(self):
        return self.apellidos + " " + self.nombres

class Medico(models.Model):
    """ Representa al medico del paciente """
    nombres = models.CharField(max_length=256)
    apellidos = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)
    telefonos = models.CharField(max_length=50)
    area = models.CharField(max_length=100)

    def __unicode__(self):
        return self.apellidos + " " + self.nombres



class Paciente(models.Model):
    """Modelo que representa a un paciente de la clinica"""

    GRUPO_SANGUINEO_CHOICES = (
        ("A+", "A+"),
        ("O+", "O+"),
        ("O-", "O-") #Faltan mas opciones
    )
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Femenino")
    )
    nombres = models.CharField(max_length=256)
    apellidos = models.CharField(max_length=256)
    lugar_nacimiento = models.CharField("lugar de nacimiento", max_length=30)
    fecha_nacimiento = models.DateField("fecha de nacimiento")
    fecha_registro = models.DateField("fecha de registro",
                                     auto_now_add=True) #Autoregistro con la fecha de creacion
    nacionalidad = models.CharField(max_length=30)
    grupo_sanguineo = models.CharField("grupo sanguineo",
                                       choices=GRUPO_SANGUINEO_CHOICES,
                                       max_length=4)
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=1)
    familiares = models.ManyToManyField(Familiar)
    def __unicode__(self):
        return self.apellidos + " " + self.nombres


