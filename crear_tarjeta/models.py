from django.db import models

class TarjetaHSEQ(models.Model):

    fecha = models.DateField(verbose_name='Fecha de Creación')
    sitio = models.CharField(max_length=255, verbose_name='Sitio de Observación')
    numero = models.IntegerField(verbose_name='Número')
    nombre_reporta = models.CharField(max_length=255, verbose_name='Nombre de quien Reporta')
    a_quien_reporta = models.CharField(max_length=255, verbose_name='A quien Reporta')
    descripcion_observacion = models.TextField(verbose_name='Descripción de la Observación')
    accion_observacion = models.TextField(verbose_name='Acción C/P/M')

    acto_condicionesA = models.BooleanField(default=False, verbose_name='a) Ejecuta trabajos con procedimientos inadecuados omitiendo normas de seguridad, salud, ambiente y calidad')
    acto_condicionesB = models.BooleanField(default=False, verbose_name='b) No utiliza, uso inadecuado de los elementos de protección personal')
    acto_condicionesC = models.BooleanField(default=False, verbose_name='c) Condiciones ambientales, manejo y disposición de residuos sólidos y liquidos inadecuado')
    acto_condicionesD = models.BooleanField(default=False, verbose_name='d) Uso inadecuado de reciclaje o ahorro de agua luz y  papel')
    acto_condicionesE = models.BooleanField(default=False, verbose_name='e) Manipulación, almacenamiento y uso inadecuado de sustancias químicas')
    acto_condicionesF = models.BooleanField(default=False, verbose_name='f) Área inadecuadas y en condiciones deficientes de orden y aseo')
    acto_condicionesG = models.BooleanField(default=False, verbose_name='g) Uso o comportamiento inadecuado de vehiculos o sin equipos de seguridad, mal estadox exceso de velocidad, mala manipulación de cargas')
    acto_condicionesH = models.BooleanField(default=False, verbose_name='h) Equipos de emergencia en mal estado o incompleto, falta de señalización o demarcación')
    acto_condicionesI = models.BooleanField(default=False, verbose_name='i) No uso o uso inadecuado de equipo de trabajo en alturas o izaje')
    acto_condicionesJ = models.BooleanField(default=False, verbose_name='j) Manejo de equipos y herramientas inadecuados o en mal estado')
    acto_condicionesK = models.BooleanField(default=False, verbose_name='k) Comportamiento seguro felicitaciones y reconocimientos')

    observacion_abierta = models.BooleanField(default=True, verbose_name='Observación Abierta')
    observacion_cerrada = models.BooleanField(default=False, verbose_name='Observación Cerrada')

    def __str__(self):
        return f"{self.sitio} - {self.fecha}"

    class Meta:
        verbose_name = "Tarjeta HSEQ"
        verbose_name_plural = "Tarjetas HSEQ"

