from rest_framework import serializers

from study.models import Lesson, Course, Subscription
from study.validators import TitleValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [TitleValidator(field='link_to_the_video')]


class CourseSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_subscribed(self, obj):
        user = self.context['request'].user  # Получаем текущего пользователя
        return Subscription.objects.filter(user=user, course=obj).exists()  # Проверяем, есть ли подписка


class CourseDataSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_count_lesson(self, course):
        """Кол-во уроков в курсе"""
        return course.lesson_set.count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        return Subscription.objects.filter(user=user, course=obj).exists()

    class Meta:
        model = Course
        fields = ('title', 'description', 'count_lesson', 'lessons', 'is_subscribed')


