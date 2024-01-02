from django import forms
from .models import TarjetaHSEQ

class TarjetaHSEQForm(forms.ModelForm):
    class Meta:
        model = TarjetaHSEQ
        fields = [
            'fecha', 'sitio', 'numero', 'nombre_reporta', 'a_quien_reporta',
            'descripcion_observacion', 'accion_observacion',
            'acto_condicionesA', 'acto_condicionesB', 'acto_condicionesC',
            'acto_condicionesD', 'acto_condicionesE', 'acto_condicionesF',
            'acto_condicionesG', 'acto_condicionesH', 'acto_condicionesI',
            'acto_condicionesJ', 'acto_condicionesK',
            'observacion_abierta', 'observacion_cerrada'
        ]
        widgets = {
            'fecha': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha', 'type': 'date'}),
            'sitio': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_reporta': forms.TextInput(attrs={'class': 'form-control'}),
            'a_quien_reporta': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_observacion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'accion_observacion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            # Campos booleanos para acto_condiciones
            'acto_condicionesA': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'acto_condicionesB': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'acto_condicionesC': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'acto_condicionesD': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'acto_condicionesE': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'acto_condicionesF': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'acto_condicionesG': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'acto_condicionesH': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'acto_condicionesI': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'acto_condicionesJ': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'acto_condicionesK': forms.CheckboxInput(attrs={'class': 'form-check-input'}),


            # ... incluir todos los demás campos booleanos de acto_condiciones ...
            'observacion_abierta': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'observacion_cerrada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'fecha': 'Fecha de Creación',
            'sitio': 'Sitio de Observación',
            'numero': 'Número',
            'nombre_reporta': 'Nombre de quien Reporta',
            'a_quien_reporta': 'A quien Reporta',
            'descripcion_observacion': 'Descripción de la Observación',
            'accion_observacion': 'Acción Correctiva/Preventiva/Mejora',
            # Etiquetas para campos booleanos de acto_condiciones
            'acto_condicionesA': 'a) Ejecuta trabajos con procedimientos inadecuados',
            'acto_condicionesB': 'b) No utiliza, uso inadecuado de los elementos de protección personal',
            'acto_condicionesC': 'c) Condiciones ambientales, manejo y disposición de residuos sólidos y liquidos inadecuado',
            'acto_condicionesD': 'd) Uso inadecuado de reciclaje o ahorro de agua luz y  papel',
            'acto_condicionesE': 'e) Manipulación, almacenamiento y uso inadecuado de sustancias químicas',
            'acto_condicionesF': 'f) Área inadecuadas y en condiciones deficientes de orden y aseo',
            'acto_condicionesG': 'g) Uso o comportamiento inadecuado de vehiculos o sin equipos de seguridad, mal estadox exceso de velocidad, mala manipulación de cargas',
            'acto_condicionesH': 'h) Equipos de emergencia en mal estado o incompleto, falta de señalización o demarcación',
            'acto_condicionesI': 'i) No uso o uso inadecuado de equipo de trabajo en alturas o izaje',
            'acto_condicionesJ': 'j) Manejo de equipos y herramientas inadecuados o en mal estado',
            'acto_condicionesK': 'k) Comportamiento seguro felicitaciones y reconocimientos',
            # ... incluir etiquetas para todos los demás campos booleanos de acto_condiciones ...
            'observacion_abierta': 'Observación Abierta',
            'observacion_cerrada': 'Observación Cerrada',
        }

    def __init__(self, *args, **kwargs):
        super(TarjetaHSEQForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False


