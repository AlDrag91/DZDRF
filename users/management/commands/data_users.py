from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Добавляет пользователей"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro',
            first_name='Аликсей',
            last_name='Admin',
            is_staff=True,
            is_superuser=True,

        )

        user.set_password('qwerty123')
        user.save()

        user = User.objects.create(
            email='manager@sky.pro',
            first_name='Дмитрий',
            last_name='user',
            is_staff=True,
            is_superuser=False,

        )

        user.set_password('qwerty123')
        user.save()

        user = User.objects.create(
            email='user_service@sky.pro',
            first_name='Максим',
            last_name='user_service',
            is_staff=True,
            is_superuser=False,

        )

        user.set_password('qwerty123')
        user.save()
