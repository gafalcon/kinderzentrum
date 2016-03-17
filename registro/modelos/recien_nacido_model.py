# -*- coding: utf-8 -*-

from django.db import models

class RecienNacido(models.Model):
    "Datos del recién nacido"

    edad_madre = models.PositiveSmallIntegerField("Edad de la madre cuando nació el bebé", blank=True)

    edad_padre = models.PositiveSmallIntegerField("Edad del padre cuando nació el bebé", blank=True)

    peso = models.FloatField("peso(gr)")

    tamanio = models.FloatField("tamaño(cm)")

    diametro_encefalico = models.FloatField("diámetro encefálico(cm)")

    APGAR_1 = 0
    APGAR_5 = 1
    APGAR_10 = 2
    APGAR_DESCONOCIDO = 4
    APGAR_CHOICES = (
        (APGAR_1, "APGAR 1"),
        (APGAR_5, "APGAR 5"),
        (APGAR_10, "APGAR 10"),
        (APGAR_DESCONOCIDO, "Desconoce")
    )
    apgar_score = models.PositiveSmallIntegerField("¿Cuál fue la puntuación del apgar? Si no lo sabe podría ayudarnos con la historia clínica de su hijo(a)") 

    complicaciones_nacimiento = models.CharField("¿El niño(a) tuvo alguna de éstas complicaciones al nacer?", max_length=256, blank=True)

    tiempo_apego_precoz = models.CharField("¿Cuánto tiempo duró el apego precoz?", max_length=20, blank=True)

    tiempo_sostener_bebe = models.CharField("¿Cuánto tiempo pasó hasta que usted pudo sostener a su bebé?", max_length=50)

    tiempo_internado = models.DurationField("¿Cuánto tiempo permaneció internado(a)")

    tipo_contacto = models.CharField("¿Qué tipo de contacto tuvo con su bebé mientras estuvo internado?", max_length=246, blank=True)

    primera_lactancia = models.CharField("La primera vez que el bebé tomó leche fue con", max_length=100)
