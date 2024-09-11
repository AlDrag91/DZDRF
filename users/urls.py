from rest_framework.routers import DefaultRouter
from users.views import UserVieSet, PaymentsVieSet

from users.apps import UsersConfig

app_name = UsersConfig.name
router = DefaultRouter()
router.register('users', UserVieSet, basename='users')
router.register('payments', PaymentsVieSet, basename='payments')
urlpatterns = [
              ] + router.urls
