from django.contrib.auth.models import User
from django.core.management import BaseCommand

from userapp.models import BbUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            user_1 = BbUser.objects.create_user('ivanov', password='1234567890',
                                                email='ivanov@site.kz', age=25)
            user_2 = BbUser.objects.create_user('petrov', password='0987654321',
                                                email='petrov@site.kz', is_staff=True, age=25)
            user_3 = BbUser.objects.create_superuser('sidorov', password='0987654321',
                                                     email='sidorov@site.kz', age=25)
        except Exception as ex:
            print("Пользователи уже созданы!")
            print(ex)
