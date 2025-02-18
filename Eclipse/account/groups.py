from django.contrib.auth.models import Group

user_comun,criado = Group.objects.get_or_create('Usuarios Comun')