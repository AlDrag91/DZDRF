from django.core.management import BaseCommand

from study.models import Course, Lesson
from users.models import Payments, User


class Command(BaseCommand):
    """Добавляет платежа"""

    def handle(self, *args, **options):
        """Добавляет платежи"""

        user, created = User.objects.get_or_create(email='user_service@sky.pro')
        user = user
        course = Course.objects.get(pk=2)
        payment = Payments.objects.create(
            user=user,
            course_paid=course,
            payment_date='2023-12-06',
            payment_amount=10000.00,
            payment_method='Перевод'
        )
        payment.save()

        user, created = User.objects.get_or_create(email='admin@sky.pro')
        user = user
        course = Course.objects.get(pk=1)
        payment = Payments.objects.create(
            user=user,
            course_paid=course,
            payment_date='2023-12-06',
            payment_amount=10000.00,
            payment_method='наличные'
        )
        payment.save()

        user, created = User.objects.get_or_create(email='manager@sky.pro')
        user = user
        course = Course.objects.get(pk=1)
        payment = Payments.objects.create(
            user=user,
            course_paid=course,
            payment_date='2023-12-06',
            payment_amount=10000.00,
            payment_method='Перевод'
        )
        payment.save()

        user, created = User.objects.get_or_create(email='manager@sky.pro')
        user = user
        lesson = Lesson.objects.get(pk=3)
        payment = Payments.objects.create(
            user=user,
            lesson_paid=lesson,
            payment_date='2023-12-16',
            payment_amount=7000.00,
            payment_method='Перевод'
        )
        payment.save()


