from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, GoalViewSet
from django.urls import path
from .views import AIGenerateResponse

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)
router.register(r'goals', GoalViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/ai-response/', AIGenerateResponse.as_view(), name='ai-response'),
]
