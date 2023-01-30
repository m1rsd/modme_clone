from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import RegisterView
from users.views import StudentModelViewSet

router = DefaultRouter()
router.register('student', StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/token', TokenObtainPairView.as_view(), name='get_token'),
    path('auth/refresh-token', TokenRefreshView.as_view(), name='refresh_token'),
]
