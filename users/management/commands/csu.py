from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Создание суперпользователя'

    def handle(self, *args, **options):
        if not User.objects.filter(email="admin1@sky.pro").exists():
            user = User.objects.create(
                email="admin1@sky.pro",
                is_staff=True,
                is_active=True,
                is_superuser=True
            )
            user.set_password("1234")
            user.save()
            self.stdout.write(self.style.SUCCESS('Суперпользователь успешно создан'))
        else:
            self.stdout.write(self.style.WARNING('Суперпользователь с таким email уже существует'))