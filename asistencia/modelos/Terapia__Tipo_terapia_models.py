from django.db import models
from Tipo_terapia_model import Tipo_terapia
from Terapista_model import Terapista


class Terapia__Tipo_terapia (models.Model):
    terapia = models.ForeignKey(Terapista)
    tipo_terapia = models.ForeignKey(Tipo_terapia)