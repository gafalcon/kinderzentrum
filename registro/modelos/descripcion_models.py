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
    edad_disc_molestia = models.IntegerField(
        "¿A qué edad notaron estas molestias?",
        blank=True,
    )
    tratamiento = models.BooleanField("¿Se encuentra en algún tratamiento?")
    lugar_tratamiento = models.CharField("¿Dónde realiza el tratamiento?",
                                         max_length=256, blank=True)
    limitaciones_movimiento = models.IntegerField(
        "¿Existe alguna limitación con sus movimientos?",
        choices=LIMITACIONES_OPTIONS)

    areas_dificultad = models.CharField("¿Ha presentado su hijo(a) algún tipo de dificultad en éstas áreas?", max_length=256, blank=True)
    had_convulsion = models.SmallIntegerField("¿Ha sentido convulsiones?",
                                            choices=LIMITACIONES_OPTIONS)
    tipo_crisis = models.CharField("¿Qué tipo de crisis tuvo durante la convlusión", max_length=256, blank=True)

    edad_crisis = models.SmallIntegerField("¿A qué edad fue la primera crisis?", blank=True)

    

class Terapia(models.Model):
    """ terapias recibidas por el paciente """
    TERAPIA_CHOICES = ((1, "REHABILITACIÓN FÍSICA"),
                       (2, "ESTIMULACIÓN TEMPRANA"),
                       (3, "INTEGRACIÓN SENSORIAL"),
                       (4, "HIPOTERAPIA"),
                       (5, "LENGUAJE"),
                       (6, "PSICOPEDAGÓGICA"),
                       (7, "TERAPIA FAMILIAR"),
                       (8, "NINGUNA"))
    tipo = models.SmallIntegerField("Tipo de terapia", choices=TERAPIA_CHOICES)
    tiempo_terapia = models.DurationField("¿Cuánto tiempo lleva realizando la terapia")
    descripcion = models.ForeignKey(Descripcion)
    

class Medicamento(models.Model):
    """ Medicamento recetado para convulsiones """
    nombre = models.CharField("nombre del medicamento", max_length=100)
    dosis_diaria = models.IntegerField()
    descripcion = models.ForeignKey(Descripcion)
