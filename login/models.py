from django.db import models


class UserRequest(models.Model):
    
    username = models.CharField(max_length=100, verbose_name="Nombre de Usuario")
    email = models.EmailField(verbose_name="Correo Electrónico")
    first_name = models.CharField(max_length=100, verbose_name="Nombre", blank=True)
    last_name = models.CharField(max_length=100, verbose_name="Apellido", blank=True)
    reason_for_request = models.TextField(verbose_name="Motivo de la Solicitud")
    request_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Solicitud")
    is_approved = models.BooleanField(default=False, verbose_name="Aprobado")

    def __str__(self):
        return f"Solicitud de {self.username} - {('Aprobada' if self.is_approved else 'Pendiente')}"

    class Meta:
        verbose_name = "Solicitud de Registro de Usuario"
        verbose_name_plural = "Solicitudes de Registro de Usuarios"

