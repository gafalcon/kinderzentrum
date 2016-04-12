# -*- coding: utf-8 -*-
from django.db import models


class Terapista(models.Model):
    """ Representa el terapista del paciente """

    cedula = models.CharField(max_length=10)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=256)
    telefonos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __unicode__(self):
        return self.apellidos + " " + self.nombres