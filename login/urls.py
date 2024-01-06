from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),  # Página de inicio de sesión
    path('home/', views.home, name='home'),  # Página de inicio post-login
    path('signout/', views.signout, name='signout'),  # Ruta para cerrar sesión
    #path('register/', views.register, name='register'),  # Ruta para el formulario de registro
    path('register/request', views.register_request, name='register_request'),  # Ruta para procesar solicitudes de registro
]
