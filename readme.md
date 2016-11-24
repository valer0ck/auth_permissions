# Custom auth permissions

Code to create custom permissions to Django User model using signal post_migrate

By default django create 3 permissions to all models (create, edit and remove) but there is not permissions to view. Custom permissions can be created at models. Our models can inherit from User, but permissions created belong to that model, not to User.

Sender that create custom permissions is accounts app. I tried to create custom permissions using as sender to Auth models and other signals and with new Dbs and already created Dbs without success. This error was raised all time 'django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.'

## Configuration

At installed apps add

```
INSTALLED_APPS = [
    ...
    'account.apps.AccountConfig',
    ...
]
```

and type python manage.py migrate

Test done to Django 1.10.3
