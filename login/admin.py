from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Registra el modelo User solo si aún no está registrado
if not admin.site.is_registered(User):
    admin.site.register(User, UserAdmin)









