from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.views import PaymentsVieSet, RegisterView, UserViewSet, MyTokenObtainPairView

from users.apps import UsersConfig

from django.urls import path, include

app_name = UsersConfig.name
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register('payments', PaymentsVieSet, basename='payments')
urlpatterns = [
                  path('', include(router.urls)),
                  path('login/', MyTokenObtainPairView.as_view(), name='login'),
                  path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('register/', RegisterView.as_view(), name='auth_register')
              ] + router.urls
