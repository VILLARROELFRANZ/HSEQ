from django import forms


class UserRequestForm(forms.Form):
    
    # Definir los campos que deseas incluir en el formulario de solicitud de registro
    username = forms.CharField(label="Nombre de Usuario", max_length=100, required=True)
    email = forms.EmailField(label="Correo Electrónico", required=True)
    first_name = forms.CharField(label="Nombre", max_length=100, required=False)
    last_name = forms.CharField(label="Apellido", max_length=100, required=False)
    reason_for_request = forms.CharField(label="Motivo de la Solicitud", widget=forms.Textarea, required=True)

    # Puedes añadir más campos según tus necesidades

    def clean_email(self):
        # Aquí puedes agregar lógica adicional para validar el correo electrónico, si lo necesitas
        email = self.cleaned_data['email']
        # Ejemplo de validación (personalízalo según tus necesidades)
        if "ejemplo.com" not in email:
            raise forms.ValidationError("Por favor, utiliza un correo electrónico válido.")
        return email

    # Si necesitas más validaciones personalizadas, puedes añadirlas aquí



