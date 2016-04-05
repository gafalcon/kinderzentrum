# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from .descripcion_models import *
from .medico_model import Medico
from .historial_madre_models import *
from .nacimiento_models import *
from .familiars_models import DatosFamiliaresOtros
from .recien_nacido_model import RecienNacido
from .alimentacion_models import AlimentacionCostumbres
from .primeros_dias_model import PrimerosDias


class Paciente(models.Model):
    """Modelo que representa a un paciente de la clinica"""

    GRUPO_SANGUINEO_CHOICES = [('o+','O+'),
                               ('o-','O-'),
                               ('a+','A+'),
                               ('a-','A-'),
                               ('b+','B+'),
                               ('b-','B-'),
                               ('ab+','AB+'),
                               ('ab-','AB-')]

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
                                       max_length=4, blank=False)
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=1, blank=False, default="--")

    medico = models.OneToOneField(Medico)
    descripcion = models.OneToOneField(Descripcion)
    historial_madre = models.OneToOneField(HistorialMadre)
    gestacion = models.OneToOneField(Gestacion)
    nacimiento = models.OneToOneField(Nacimiento)
    recien_nacido = models.OneToOneField(RecienNacido)
    primeros_dias = models.OneToOneField(PrimerosDias)
    alimentacion = models.OneToOneField(AlimentacionCostumbres)
    datos_familiares = models.OneToOneField(DatosFamiliaresOtros)

    def __unicode__(self):
        return self.apellidos + " " + self.nombres


