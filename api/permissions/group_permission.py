import os
import logging
import django
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DrJwt.settings')

django.setup()

GROUPS = ['admin', 'user']
MODELS = ['user']

for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)

    for model in MODELS:
        if new_group.name == 'admin':
            PERMISSIONS = ['view', 'change', 'add', 'delete']

            for permission in PERMISSIONS:
                name = 'Can {} {}'.format(permission, model)
                print("Creating {}".format(name))

                try:
                    model_add_perm = Permission.objects.get(name=name)

                except Permission.DoesNotExist:
                    logging.warning("Permission not found with name '{}'.".format(name))
                    continue

                new_group.permissions.add(model_add_perm)

        else:
            PERMISSIONS = ['view']

            for permission in PERMISSIONS:
                name = 'Can {} {}'.format(permission, model)
                print("Creating {}".format(name))

                try:
                    model_add_perm = Permission.objects.get(name=name)

                except Permission.DoesNotExist:
                    logging.warning("Permission not found with name '{}'.".format(name))
                    continue

                new_group.permissions.add(model_add_perm)

    print("Created default group and permissions.")
