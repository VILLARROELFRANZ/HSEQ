from django.urls import path
from . import views  # Importa las vistas de tu aplicación

urlpatterns = [
    path('', views.signin, name='signin'),  # Página de inicio post-login
    path('home/', views.home, name='home'),  # Página de inicio de sesión
    path('signout/', views.signout, name='signout'),  # Ruta para cerrar sesión
]