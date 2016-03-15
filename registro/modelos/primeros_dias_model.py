# -*- coding: utf-8 -*-

from django.db import models


class PrimerosDias(models.Model):
    "Primeros días de vida del niño(a)"
    clinica_permanencia = models.CharField("¿Cuál fue la clínica u hospital en la que permaneció el niño(a)", max_length=100, blank=True)

    dias_permanencia = models.PositiveIntegerField("Indique los días de permanencia", blank=True)

    situaciones_despues_nacimiento = models.CharField("¿Presentó su bebé alguna de éstas situaciones después del nacimiento", max_length=256, blank=True)

    icteria = models.CharField("¿Hubo algún tratamiento por icteria", max_length=10)

    tratamiento_icteria = models.CharField("¿Cuál fue el tratamiento por icteria?", max_length=256, blank=True)

    examenes = models.CharField("¿Le realizaron al recién nacido algún tipo de exámen?", max_length=100, blank=True)

    veces_despertar_noche = models.PositiveSmallIntegerField("¿Cuántas veces se despertaba el recién nacido?", default=0)

    lugar_dormir = models.CharField("¿Dónde dormía el bebé", max_length=50)

    descripcion_bebe = models.CharField("Describa a su bebé los 3 primeros meses de vida", max_length=256, blank=True)

    descripcion_madre = models.CharField("¿Cómo se sentía usted esos 3 primeros meses?", max_length=256, blank=True)
    
