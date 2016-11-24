from __future__ import unicode_literals

from django.apps import AppConfig
from django.db.models.signals import post_migrate
from .signals import add_user_permissions


class AccountConfig(AppConfig):
    name = 'Account'

    def ready(self):
        # Signal to create custom auth permissions
        post_migrate.connect(add_user_permissions, sender=self)
