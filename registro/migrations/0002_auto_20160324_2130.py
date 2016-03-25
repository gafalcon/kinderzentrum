# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terapista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.CharField(max_length=10)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=256)),
                ('telefonos', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField(verbose_name='fecha de nacimiento')),
                ('grupo_sanguineo', models.CharField(max_length=4, verbose_name='grupo sanguineo', choices=[('A+', 'A+'), ('A-', 'A-'), ('O+', 'O+'), ('O-', 'O-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')])),
                ('especialidad', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='alimentacioncostumbres',
            name='lugar_comida_media_manana',
            field=models.CharField(max_length=50, verbose_name=b'media ma\xc3\xb1ana', blank=True),
        ),
        migrations.AlterField(
            model_name='alimentacioncostumbres',
            name='lugar_comida_media_tarde',
            field=models.CharField(max_length=50, verbose_name=b'media tarde', blank=True),
        ),
        migrations.AlterField(
            model_name='alimentacioncostumbres',
            name='lugar_comida_otro',
            field=models.CharField(max_length=50, verbose_name=b'otro', blank=True),
        ),
        migrations.AlterField(
            model_name='alimentacioncostumbres',
            name='tiempo_leche_materna',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, b'1 - 4 Meses'), (1, b'5 - 6 Meses'), (2, b'7 - 8 Meses'), (3, b'9 - 12 Meses'), (4, b'13 - 18 Meses'), (5, b'19 - 24 Meses')]),
        ),
        migrations.AlterField(
            model_name='datosfamiliaresotros',
            name='alteracion_desarrollo',
            field=models.NullBooleanField(verbose_name=b'\xc2\xbfHa existido alg\xc3\xban tipo de alteraci\xc3\xb3n en su desarrollo?'),
        ),
        migrations.AlterField(
            model_name='datosfamiliaresotros',
            name='hermano_transtorno',
            field=models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfCu\xc3\xa1l de los hermanos? (Orden en que naci\xc3\xb3)', blank=True),
        ),
        migrations.AlterField(
            model_name='datosfamiliaresotros',
            name='numero_hermanos',
            field=models.PositiveSmallIntegerField(verbose_name=b'N\xc3\xbamero de hermanos'),
        ),
        migrations.AlterField(
            model_name='datosfamiliaresotros',
            name='orientacion_a_institucion',
            field=models.CharField(max_length=100, verbose_name=b'Qui\xc3\xa9n los orient\xc3\xb3 a \xc3\xa9sta instituci\xc3\xb3n?'),
        ),
        migrations.AlterField(
            model_name='datosfamiliaresotros',
            name='tipo_enfermedad_parientes',
            field=models.CharField(max_length=256, verbose_name=b'Detallar el tipo de enfermedad que se ha presentado en los parientes', blank=True),
        ),
        migrations.AlterField(
            model_name='datosfamiliaresotros',
            name='transtorno',
            field=models.CharField(max_length=50, verbose_name=b'Qu\xc3\xa9 transtorno?', blank=True),
        ),
        migrations.AlterField(
            model_name='datosfamiliaresotros',
            name='transtorno_hermanos',
            field=models.NullBooleanField(verbose_name=b'\xc2\xbfAlguno de los hermanos tiene alg\xc3\xban tipo de transtorno?'),
        ),
        migrations.AlterField(
            model_name='hermano',
            name='fecha_nacimiento',
            field=models.DateField(verbose_name=b'Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='grupo_sanguineo',
            field=models.CharField(max_length=4, verbose_name='grupo sanguineo', choices=[('A+', 'A+'), ('A-', 'A-'), ('O+', 'O+'), ('O-', 'O-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')]),
        ),
        migrations.AlterField(
            model_name='primerosdias',
            name='clinica_permanencia',
            field=models.CharField(max_length=100, verbose_name=b'\xc2\xbfCu\xc3\xa1l fue la cl\xc3\xadnica u hospital en la que permaneci\xc3\xb3 el ni\xc3\xb1o(a)?', blank=True),
        ),
        migrations.AlterField(
            model_name='primerosdias',
            name='descripcion_bebe',
            field=models.CharField(max_length=256, verbose_name=b'Describa a su beb\xc3\xa9 los 3 primeros meses de vida'),
        ),
        migrations.AlterField(
            model_name='primerosdias',
            name='descripcion_madre',
            field=models.CharField(max_length=256, verbose_name=b'\xc2\xbfC\xc3\xb3mo se sent\xc3\xada usted esos 3 primeros meses?'),
        ),
        migrations.AlterField(
            model_name='primerosdias',
            name='icteria',
            field=models.NullBooleanField(verbose_name=b'\xc2\xbfHubo alg\xc3\xban tratamiento por icteria'),
        ),
        migrations.AlterField(
            model_name='primerosdias',
            name='lugar_dormir',
            field=models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfD\xc3\xb3nde dorm\xc3\xada el beb\xc3\xa9?'),
        ),
        migrations.AlterField(
            model_name='primerosdias',
            name='situaciones_despues_nacimiento',
            field=models.CharField(max_length=256, verbose_name=b'\xc2\xbfPresent\xc3\xb3 su beb\xc3\xa9 alguna de \xc3\xa9stas situaciones despu\xc3\xa9s del nacimiento?', blank=True),
        ),
        migrations.AlterField(
            model_name='reciennacido',
            name='apgar_score',
            field=models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfCu\xc3\xa1l fue la puntuaci\xc3\xb3n del apgar? Si no lo sabe podr\xc3\xada ayudarnos con la historia cl\xc3\xadnica de su hijo(a)'),
        ),
        migrations.AlterField(
            model_name='reciennacido',
            name='complicaciones_nacimiento',
            field=models.CharField(max_length=256, verbose_name=b'\xc2\xbfEl ni\xc3\xb1o(a) tuvo alguna de \xc3\xa9stas complicaciones al nacer?', blank=True),
        ),
        migrations.AlterField(
            model_name='reciennacido',
            name='primera_lactancia',
            field=models.PositiveSmallIntegerField(verbose_name=b'La primera vez que el beb\xc3\xa9 tom\xc3\xb3 leche fue con'),
        ),
        migrations.AlterField(
            model_name='reciennacido',
            name='tiempo_apego_precoz',
            field=models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfCu\xc3\xa1nto tiempo dur\xc3\xb3 el apego precoz?', blank=True),
        ),
        migrations.AlterField(
            model_name='reciennacido',
            name='tiempo_internado',
            field=models.DurationField(verbose_name=b'\xc2\xbfCu\xc3\xa1nto tiempo permaneci\xc3\xb3 internado(a)?', blank=True),
        ),
        migrations.AlterField(
            model_name='reciennacido',
            name='tiempo_sostener_bebe',
            field=models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfCu\xc3\xa1nto tiempo pas\xc3\xb3 hasta que usted pudo sostener a su beb\xc3\xa9?'),
        ),
        migrations.AlterField(
            model_name='reciennacido',
            name='tipo_contacto',
            field=models.PositiveSmallIntegerField(verbose_name=b'\xc2\xbfQu\xc3\xa9 tipo de contacto tuvo con su beb\xc3\xa9 mientras estuvo internado?', blank=True),
        ),
        migrations.AlterField(
            model_name='terapia',
            name='tipo',
            field=models.SmallIntegerField(verbose_name=b'Tipo de terapia', choices=[(1, b'REHABILITACI\xc3\x93N F\xc3\x8dSICA'), (2, b'ESTIMULACI\xc3\x93N TEMPRANA'), (3, b'INTEGRACI\xc3\x93N SENSORIAL'), (4, b'HIPOTERAPIA'), (5, b'LENGUAJE'), (6, b'PSICOPEDAG\xc3\x93GICA'), (7, b'TERAPIA FAMILIAR'), (8, b'NINGUNA')]),
        ),
    ]
