from django.db import models
from users.models import User
from users.constants import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название курса')
    preview = models.ImageField(upload_to='course/course', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    student = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Название курса')
    title = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='course/lesson', verbose_name='Превью', **NULLABLE)
    link_to_the_video = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
