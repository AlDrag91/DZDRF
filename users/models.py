from django.contrib.auth.models import AbstractUser
from django.db import models
from study.models import Course, Lesson
from users.constants import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=35, verbose_name='город', **NULLABLE)
    country = models.CharField(max_length=25, verbose_name='Страна', **NULLABLE)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now=True)
    course_paid = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)
    lesson_paid = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20,
                                      choices=[('наличные', 'Наличные'), ('Перевод', 'Перевод на счет')], **NULLABLE)

    def __str__(self):
        return f"{self.user} - {self.course_paid} - {self.lesson_paid} - {self.payment_amount}"
