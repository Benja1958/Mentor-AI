from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, GoalViewSet

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)
router.register(r'goals', GoalViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
