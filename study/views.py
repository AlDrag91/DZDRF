from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from study.models import Course, Lesson
from study.seriliazers import CourseSerializer, LessonSerializer, CourseDataSerializer
from users.permissions import IsModerator, IsOwner

"""ViewSet для курсов"""


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDataSerializer
        return CourseSerializer

    def get_permissions(self):
        if self.action in ["retrieve", "update"]:
            self.permission_classes = (IsModerator | IsOwner,)
        elif self.action == "create":
            self.permission_classes = (~IsModerator,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModerator | IsOwner,)
        return super().get_permissions()

    def perform_create(self, serializer):
        course = serializer.save()
        course.student = self.request.user
        course.save()


"""Generics для уроков"""


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator, IsAuthenticated)

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.student = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    parser_classes = [IsModerator]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsModerator | IsOwner, IsAuthenticated)


class LessonUpdateAPIView(generics.UpdateAPIView):
    parser_classes = [IsModerator]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsModerator | IsOwner, IsAuthenticated)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, ~IsModerator | IsOwner)
