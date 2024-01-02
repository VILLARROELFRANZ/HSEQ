from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_tarjetas, name='lista_tarjetas'),
    path('nueva/', views.crear_tarjeta, name='crear_tarjeta'),
    path('detalle/<int:pk>/', views.detalle_tarjeta, name='detalle_tarjeta'),
    path('editar/<int:pk>/', views.editar_tarjeta, name='editar_tarjeta'),
    path('cerrar/<int:pk>/', views.cerrar_tarjeta, name='cerrar_tarjeta'),
    path('eliminar/<int:pk>/', views.eliminar_tarjeta, name='eliminar_tarjeta'),
    path('publico/', views.crear_tarjeta_publico, name='crear_tarjeta_publico'),
    path('confirmacion-envio/', views.confirmacion_envio, name='confirmacion_envio'),

]






