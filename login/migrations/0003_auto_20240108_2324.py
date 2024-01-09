from django.db import migrations
from django.contrib.auth.models import User

def create_predefined_users(apps, schema_editor):
    predefined_users = [
        {'username': 'user1', 'password': 'password1', 'email': 'user1@example.com'},
        {'username': 'user2', 'password': 'password2', 'email': 'user2@example.com'},
        {'username': 'user3', 'password': 'password3', 'email': 'user3@example.com'},
        {'username': 'user4', 'password': 'password4', 'email': 'user4@example.com'},
    ]

    for user_data in predefined_users:
        user, created = User.objects.get_or_create(username=user_data['username'], email=user_data['email'])
        if created:
            user.set_password(user_data['password'])
            user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_useraccesslog_delete_userresquest'),  # Asegúrate de que esta sea la última migración
    ]

    operations = [
        migrations.RunPython(create_predefined_users),
    ]
