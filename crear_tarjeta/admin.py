from django.contrib import admin
from .models import TarjetaHSEQ
from .forms import TarjetaHSEQForm

@admin.register(TarjetaHSEQ)
class TarjetaHSEQAdmin(admin.ModelAdmin):
    form = TarjetaHSEQForm
    list_display = ('fecha', 'sitio', 'numero', 'nombre_reporta', 'a_quien_reporta', 'observacion_abierta', 'observacion_cerrada')
    list_filter = ('observacion_abierta', 'observacion_cerrada', 'fecha', 'sitio')
    search_fields = ('sitio', 'nombre_reporta', 'descripcion_observacion')
    date_hierarchy = 'fecha'

    def get_readonly_fields(self, request, obj=None):
        if obj:  # obj is not None, so this is an edit
            return ['fecha', 'sitio']  # These fields will be readonly when editing
        else:
            return []  # No fields will be readonly when creating


