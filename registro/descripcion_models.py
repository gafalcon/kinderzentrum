# -*- coding: utf-8 -*-
from django.db import models

class Descripcion(models.Model):
    """ Descripcion del problema del paciente """
    LIMITACIONES_OPTIONS = ((1, "SI"), (2, "NO"), (3, "DESCONOCE"))
    preocupacion = models.CharField(
        "¿Qué le preocupa de su hijo? Algo especial que le llame la atención",
        max_length=500
    )
    disc_molestias = models.CharField(
        "¿Quién descubrió estas molestias?",
        blank=True,
        max_length=256
    )
    fecha_disc_molestia = models.CharField(
        "¿Cuándo lo empezaron a notar?",
        blank=True,
        max_length=30
    )
    tratamiento = models.BooleanField("¿Se encuentra en algún tratamiento?")
    lugar_tratamiento = models.CharField("Lugar de Tratamiento",
                                         max_length=256, blank=True)
    orientador_institucion = models.CharField("¿Quién los orientó a ésta institución?",
                                              max_length=100, blank=True)
    limitaciones_movimiento = models.IntegerField(
        "¿Existe alguna limitación con sus movimientos?",
        choices=LIMITACIONES_OPTIONS)

    areas_dificultad = None #Multiple choice
    had_convulsion = models.SmallIntegerField("¿Ha sentido convulsiones?",
                                            choices=LIMITACIONES_OPTIONS)

class Terapia(models.Model):
    """ terapias recibidas por el paciente """
    TERAPIA_CHOICES = ((1, "REHABILITACIÓN FÍSICA"),
                       (2, "ESTIMULACIÓN TEMPRANA"))
    tipo = models.SmallIntegerField("tipo de terapia", choices=TERAPIA_CHOICES)
    tiempo_terapia = models.DurationField("¿Cuánto tiempo lleva realizando la terapia")


class Convulsion(models.Model):
    """ Convulsion que haya presentado el paciente """
    crisis = models.CharField("¿Qué tipo de crisis tuvo en la convulsión?", max_length=300)
    edad = models.IntegerField("¿A qué edad fue la primera crisis?")

class Medicamento(models.Model):
    """ Medicamento recetado para convulsiones """
    nombre = models.CharField("nombre del medicamento", max_length=100)
    dosis_diaria = models.IntegerField()
