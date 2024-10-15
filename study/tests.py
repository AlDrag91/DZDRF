from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from study.models import Course, Lesson, Subscription
from users.models import User


class LessonAPITests(APITestCase):
    User = get_user_model()

    def setUp(self):
        """Создаем пользователей"""
        self.user1 = User.objects.create(email='admin@sky.pro', password='qwerty123', is_superuser=True)
        """Создаем курсы"""
        self.course = Course.objects.create(title="Test Course1")
        """Создаем уроки"""
        self.lesson1 = Lesson.objects.create(title="Lesson 1", course=self.course)
        self.lesson2 = Lesson.objects.create(title="Lesson 2", course=self.course)

    def authenticate_user(self, user):
        self.client.force_authenticate(user=user)

    def test_create_lesson(self):
        """Тест создания урока"""
        self.authenticate_user(self.user1)
        response = self.client.post('lesson/create/', {'title': 'Lesson 3', 'course': self.course.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 3)

    # def test_update_lesson(self):
    #     """Тест изменения урока"""
    #     self.authenticate_user(self.user1)
    #     response = self.client.put(f'/lessons/{self.lesson1.id}/', {'title': 'Updated Lesson 1'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.lesson1.refresh_from_db()
    #     self.assertEqual(self.lesson1.title, 'Updated Lesson 1')
    #
    # def test_delete_lesson(self):
    #     """Тест удаления урока"""
    #     self.authenticate_user(self.user1)
    #     response = self.client.delete(f'/lessons/{self.lesson1.id}/')
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(Lesson.objects.count(), 1)
    #
    # def test_subscribe_to_course(self):
    #     """Тест подписание на курс"""
    #     self.authenticate_user(self.user1)
    #     response = self.client.post('/course/subscribe/', {'course_id': self.course.id})
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertTrue(Subscription.objects.filter(user=self.user1, course=self.course).exists())
    #
    # def test_unsubscribe_from_course(self):
    #     """Тест отписки от курса"""
    #     self.authenticate_user(self.user1)
    #     Subscription.objects.create(user=self.user1, course=self.course)
    #     response = self.client.delete('/course/subscribe/', {'course_id': self.course.id})
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertFalse(Subscription.objects.filter(user=self.user1, course=self.course).exists())
