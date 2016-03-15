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

    GRUPO_SANGUINEO_CHOICES = (
        ("A+", "A+"),
        ("O+", "O+"),
        ("O-", "O-") #Faltan mas opciones
    )
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Femenino")
    )

    VIVE_CON_PADRES = 0
    VIVE_CON_PAPA = 1
    VIVE_CON_MAMA = 2
    VIVE_CON_APODERADO = 3
    VIVE_CON_PADRE_ADOPTIVO = 4
    VIVE_CON_ABUELOS = 5
    VIVE_CON_GUARDERIA = 6
    VIVE_CON_OTROS = 7
    VIVE_CON_CHOICES = (
        (VIVE_CON_PADRES, "Padres"),
        (VIVE_CON_PAPA, "Papá"),
        (VIVE_CON_MAMA, "Mamá"),
        (VIVE_CON_APODERADO, "Apoderado"),
        (VIVE_CON_PADRE_ADOPTIVO, "Padre adoptivo"),
        (VIVE_CON_ABUELOS, "Abuelos"),
        (VIVE_CON_GUARDERIA, "Guardería"),
        (VIVE_CON_OTROS, "Otros")

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


