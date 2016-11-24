from django.apps import apps


def add_user_permissions(sender, **kwargs):
    """
        Create custom permissions to auth app to see users and update password
        It is called from apps.py
    """

    User = apps.get_model("auth", "User")
    ContentType = apps.get_model("contenttypes", "ContentType")
    Permission = apps.get_model("auth", "Permission")

    content_type = ContentType.objects.get_for_model(User)
    Permission.objects.get_or_create(
        codename='view_user', name='Can see users',
        content_type=content_type)
    Permission.objects.get_or_create(
        codename='update_password', name='Can update password',
        content_type=content_type)
