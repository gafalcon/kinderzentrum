# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terapia__Tipo_terapia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Terapista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=256)),
                ('telefonos', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_terapia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.FloatField()),
                ('nombre', models.CharField(max_length=200)),
                ('tiempo', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='terapia__tipo_terapia',
            name='terapista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.Terapista'),
        ),
        migrations.AddField(
            model_name='terapia__tipo_terapia',
            name='tipo_terapia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.Tipo_terapia'),
        ),
    ]
