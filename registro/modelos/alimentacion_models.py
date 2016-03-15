# -*- coding: utf-8 -*-

from django.db import models


class AlimentacionCostumbres(models.Model):
    """Alimentación y Costumbres"""
    tiempo_leche_materna = models.CharField("¿Cuánto tiempo recibió leche materna?", max_length=25)
    motivo_suspencion_lactancia = models.CharField("¿Por qué suspendió la leche materna?", max_length=100)
    afecciones = models.CharField(max_length=100, blank=True)
    enfermedades = models.CharField(max_length=256, blank=True)
    edad_alimentacion_complementaria = models.PositiveSmallIntegerField()
    forma_alimento = models.CharField(max_length=100)
    lugar_desayuno = models.CharField(max_length=50)
    lugar_comida_media_manana = models.CharField(max_length=50)
    lugar_almuerzo = models.CharField(max_length=50)
    lugar_comida_media_tarde = models.CharField(max_length=50)
    lugar_cena = models.CharField(max_length=50)
    lugar_comida_otro = models.CharField(max_length=50)
    alimento_preferido = models.CharField(max_length=20)
    alimento_rechazado = models.CharField(max_length=20)
    apetito = models.CharField(max_length=10)
    motivo_cambios_alimentacion = models.CharField(max_length=256)


class SuplementoAlimenticio(models.Model):
    "Suplementos alimenticios consumidos por el niño(a)"
    frecuencia = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    cantidad = models.PositiveSmallIntegerField()
    alimentacion = models.ForeignKey(AlimentacionCostumbres, on_delete=models.CASCADE)
 
