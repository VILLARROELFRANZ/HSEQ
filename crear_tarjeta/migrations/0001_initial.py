# Generated by Django 5.0 on 2023-12-31 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TarjetaHSEQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de Creación')),
                ('sitio', models.CharField(max_length=255, verbose_name='Sitio de Observación')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('nombre_reporta', models.CharField(max_length=255, verbose_name='Nombre de quien Reporta')),
                ('a_quien_reporta', models.CharField(max_length=255, verbose_name='A quien Reporta')),
                ('descripcion_observacion', models.TextField(verbose_name='Descripción de la Observación')),
                ('observacion_abierta', models.BooleanField(default=True, verbose_name='Observación Abierta')),
                ('observacion_cerrada', models.BooleanField(default=False, verbose_name='Observación Cerrada')),
            ],
            options={
                'verbose_name': 'Tarjeta HSEQ',
                'verbose_name_plural': 'Tarjetas HSEQ',
            },
        ),
    ]