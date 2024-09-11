from rest_framework import serializers

from study.models import Lesson, Course


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDataSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)


    def get_count_lesson(self, course):
        """Кол-во уроков в курсе"""
        return course.lesson_set.count()

    class Meta:
        model = Course
        fields = ('title', 'description', 'count_lesson', 'lessons')
