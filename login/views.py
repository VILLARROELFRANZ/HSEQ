from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRequestForm  # Asegúrate de tener este formulario definido

@login_required
def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'form': form, 'show_register_link': True})
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form, 'show_register_link': True})

@login_required
def signout(request):
    logout(request)
    return redirect('signin')

def register_request(request):
    if request.method == 'POST':
        form = UserRequestForm(request.POST)
        if form.is_valid():
            # Aquí se manejaría la lógica para enviar un correo electrónico con la solicitud
            send_mail(
                'Nueva Solicitud de Registro de Usuario',
                'Detalles de la solicitud: ' + str(form.cleaned_data),
                settings.DEFAULT_FROM_EMAIL,
                ['villarroelfranz1@gmail.com'],  # Correo del administrador
                fail_silently=False,
            )
            return render(request, 'registration_request_sent.html')  # Plantilla de confirmación
    else:
        form = UserRequestForm()
    return render(request, 'register_request.html', {'form': form})

