# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=256)),
                ('apellidos', models.CharField(max_length=256)),
                ('nivel_studio', models.CharField(max_length=20, verbose_name='Nivel de Studio', choices=[('Superior', 'Superior'), ('Bachiller', 'Bachiller')])),
                ('direccion', models.CharField(max_length=256)),
                ('telefonos', models.CharField(max_length=50)),
                ('empresa', models.CharField(max_length=256, verbose_name='lugar de trabajo', blank=True)),
                ('direccion_empresa', models.CharField(max_length=256, verbose_name='direccion de empresa', blank=True)),
                ('jornada', models.CharField(max_length=50, verbose_name='jornada de trabajo')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=256)),
                ('apellidos', models.CharField(max_length=256)),
                ('direccion', models.CharField(max_length=256)),
                ('telefonos', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=256)),
                ('apellidos', models.CharField(max_length=256)),
                ('lugar_nacimiento', models.CharField(max_length=30, verbose_name='lugar de nacimiento')),
                ('fecha_nacimiento', models.DateField(verbose_name='fecha de nacimiento')),
                ('fecha_registro', models.DateField(auto_now_add=True, verbose_name='fecha de registro')),
                ('nacionalidad', models.CharField(max_length=30)),
                ('grupo_sanguineo', models.CharField(max_length=4, verbose_name='grupo sanguineo', choices=[('A+', 'A+'), ('O+', 'O+'), ('O-', 'O-')])),
                ('sexo', models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])),
                ('familiares', models.ManyToManyField(to='registro.Familiar')),
            ],
        ),
    ]
