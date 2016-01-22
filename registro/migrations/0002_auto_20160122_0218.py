# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad_Gestacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.SmallIntegerField()),
                ('periodo', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Convulsion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crisis', models.CharField(max_length=300, verbose_name=b'\xc2\xbfQu\xc3\xa9 tipo de crisis tuvo en la convulsi\xc3\xb3n?')),
                ('edad', models.IntegerField(verbose_name=b'\xc2\xbfA qu\xc3\xa9 edad fue la primera crisis?')),
            ],
        ),
        migrations.CreateModel(
            name='Descripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preocupacion', models.CharField(max_length=500, verbose_name=b'\xc2\xbfQu\xc3\xa9 le preocupa de su hijo? Algo especial que le llame la atenci\xc3\xb3n')),
                ('disc_molestias', models.CharField(max_length=256, verbose_name=b'\xc2\xbfQui\xc3\xa9n descubri\xc3\xb3 estas molestias?', blank=True)),
                ('fecha_disc_molestia', models.CharField(max_length=30, verbose_name=b'\xc2\xbfCu\xc3\xa1ndo lo empezaron a notar?', blank=True)),
                ('tratamiento', models.BooleanField(verbose_name=b'\xc2\xbfSe encuentra en alg\xc3\xban tratamiento?')),
                ('lugar_tratamiento', models.CharField(max_length=256, verbose_name=b'Lugar de Tratamiento', blank=True)),
                ('orientador_institucion', models.CharField(max_length=100, verbose_name=b'\xc2\xbfQui\xc3\xa9n los orient\xc3\xb3 a \xc3\xa9sta instituci\xc3\xb3n?', blank=True)),
                ('limitaciones_movimiento', models.IntegerField(verbose_name=b'\xc2\xbfExiste alguna limitaci\xc3\xb3n con sus movimientos?', choices=[(1, b'SI'), (2, b'NO'), (3, b'DESCONOCE')])),
                ('had_convulsion', models.SmallIntegerField(verbose_name=b'\xc2\xbfHa sentido convulsiones?', choices=[(1, b'SI'), (2, b'NO'), (3, b'DESCONOCE')])),
            ],
        ),
        migrations.CreateModel(
            name='Enfermedad_Madre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_desarrollo', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Gestacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sentimientos', models.CharField(max_length=200)),
                ('fecha_embarazo', models.CharField(max_length=100)),
                ('num_embarazo', models.SmallIntegerField()),
                ('nauseas_trimestre', models.SmallIntegerField()),
                ('vacuna_tetano', models.BooleanField()),
                ('comunicacion_bebe', models.CharField(max_length=500)),
                ('curso_prenatal', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Historial_madre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('perdidas_gestacionales', models.IntegerField()),
                ('hijos_muertos', models.BooleanField()),
                ('num_hijos_nacidos_muertos', models.SmallIntegerField()),
                ('num_hijos_nacidos_vivos', models.SmallIntegerField()),
                ('enfermedades_previas', models.CharField(max_length=200, verbose_name=b'\xc2\xbfEnfermedad antes de concebir al beb\xc3\xa9?', blank=True)),
                ('anticonceptivos', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'nombre del medicamento')),
                ('dosis_diaria', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nacimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_lugar_nacimiento', models.CharField(max_length=500, blank=True)),
                ('tipo_lugar_nacimiento', models.CharField(max_length=20)),
                ('semana_gestacion', models.SmallIntegerField()),
                ('tipo_nacimiento', models.CharField(max_length=100)),
                ('tipo_inicio_parto', models.CharField(max_length=30)),
                ('tipo_ruptura_agua', models.SmallIntegerField()),
                ('sentimientos', models.CharField(max_length=500)),
                ('duracion', models.SmallIntegerField()),
                ('gemelar', models.BooleanField()),
                ('primera_parte_cuerpo', models.SmallIntegerField()),
                ('complicaciones', models.CharField(max_length=200)),
                ('inyecciones', models.SmallIntegerField()),
                ('complicaciones_cordon', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Terapia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.SmallIntegerField(verbose_name=b'tipo de terapia', choices=[(1, b'REHABILITACI\xc3\x93N F\xc3\x8dSICA'), (2, b'ESTIMULACI\xc3\x93N TEMPRANA')])),
                ('tiempo_terapia', models.DurationField(verbose_name=b'\xc2\xbfCu\xc3\xa1nto tiempo lleva realizando la terapia')),
            ],
        ),
        migrations.CreateModel(
            name='Situacion_Gestacion',
            fields=[
                ('actividad_gestacion_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='registro.Actividad_Gestacion')),
            ],
            bases=('registro.actividad_gestacion',),
        ),
        migrations.AddField(
            model_name='enfermedad_madre',
            name='historial_madre',
            field=models.ForeignKey(to='registro.Historial_madre'),
        ),
        migrations.AddField(
            model_name='actividad_gestacion',
            name='historial_madre',
            field=models.ForeignKey(to='registro.Historial_madre'),
        ),
    ]
