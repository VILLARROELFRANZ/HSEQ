from django.contrib import admin
from .models import UserRequest

@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la vista de lista
    list_display = ('username', 'email', 'first_name', 'last_name', 'request_date', 'approval_status')

    # Campos para filtrar en la vista de lista
    list_filter = ('is_approved',)

    # Campos por los cuales se puede buscar en la vista de lista
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Método para mostrar una representación legible del estado de aprobación
    def approval_status(self, obj):
        return "Aprobada" if obj.is_approved else "Pendiente"
    approval_status.short_description = "Estado de Aprobación"








