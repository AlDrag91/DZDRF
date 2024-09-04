from rest_framework import viewsets

from users.models import User
from users.seriliazers import UserSerializer


class UserVieSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
