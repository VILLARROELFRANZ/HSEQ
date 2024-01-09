from django.db import models
from django.contrib.auth.models import User

class UserAccessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"

    class Meta:
        verbose_name = "Registro de Acceso de Usuario"
        verbose_name_plural = "Registros de Acceso de Usuarios"

