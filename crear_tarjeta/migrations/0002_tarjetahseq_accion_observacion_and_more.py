# Generated by Django 5.0 on 2024-01-02 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crear_tarjeta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjetahseq',
            name='accion_observacion',
            field=models.TextField(default=1, verbose_name='Acción C/P/M'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarjetahseq',
            name='acto_condicionesA',
            field=models.BooleanField(default=False, verbose_name='a) Ejecuta trabajos con procedimientos inadecuados omitiendo normas de seguridad, salud, ambiente y calidad'),
        ),
        migrations.AddField(
            model_name='tarjetahseq',
            name='acto_condicionesB',
            field=models.BooleanField(default=False, verbose_name='b) No utiliza, uso inadecuado de los elementos de protección personal'),
        ),
        migrations.AddField(
            model_name='tarjetahseq',
            name='acto_condicionesC',
            field=models.BooleanField(default=False, verbose_name='c) Condiciones ambientales, manejo y disposición de residuos sólidos y liquidos inadecuado'),
        ),
        migrations.AddField(
            model_name='tarjetahseq',
            name='acto_condicionesD',
            field=models.BooleanField(default=False, verbose_name='d) Uso inadecuado de reciclaje o ahorro de agua luz y  papel'),
        ),
        migrations.AddField(
            model_name='tarjetahseq',
            name='acto_condicionesE',
            field=models.BooleanField(default=False, verbose_name='e) Manipulación, almacenamiento y uso inadecuado de sustancias químicas'),
        ),
        migrations.AddField(
            model_name='tarjetahseq',
            name='acto_condicionesF',
            field=models.BooleanField(default=False, verbose_name='f) Área inadecuadas y en condiciones deficientes de orden y aseo'),
        ),
        migrations.AddField(
            model_name='tarjetahseq',
            name='acto_condicionesG',
            field=models.BooleanField(default=False, verbose_name='g) Uso o comportamiento inadecuado de vehiculos o sin equipos de seguridad, mal estadox exceso de velocidad, mala manipulación de cargas'),
        ),
        migrations.AddField(
            model_name='tarjetahseq',
            name='acto_condicionesH',
            field=models.BooleanField(default=False, verbose_name='h) Equipos de emergencia en mal estado o incompleto, falta de señalización o demarcación'),
        ),
        migrations.AddField(
            model_name='tarjetahseq',
            name='acto_condicionesI',
            field=models.BooleanField(default=False, verbose_name='i) No uso o uso inadecuado de equipo de trabajo en alturas o izaje'),
        ),
        migrations.AddField(
            model_name='tarjetahseq',
            name='acto_condicionesJ',
            field=models.BooleanField(default=False, verbose_name='j) Manejo de equipos y herramientas inadecuados o en mal estado'),
        ),
        migrations.AddField(
            model_name='tarjetahseq',
            name='acto_condicionesK',
            field=models.BooleanField(default=False, verbose_name='k) Comportamiento seguro felicitaciones y reconocimientos'),
        ),
    ]
