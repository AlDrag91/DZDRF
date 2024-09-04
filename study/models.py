from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    course_title = models.CharField(max_length=100, verbose_name='Название курса')
    preview = models.ImageField(upload_to='course/course', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.course_title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    course_title = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Название курса')
    lesson_title = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='course/lesson', verbose_name='Превью', **NULLABLE)
    link_to_the_video = models.GenericIPAddressField(verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.lesson_title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
