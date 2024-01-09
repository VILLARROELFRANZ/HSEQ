from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Puedes personalizar el formulario de autenticación si es necesario
class CustomAuthenticationForm(AuthenticationForm):
    # Por ejemplo, puedes agregar clases CSS a los campos
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre de usuario'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña'})





