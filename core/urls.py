from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from core.views.user import RegisterView
from core.views.task import (
    TaskAllView,
    TaskCreateView,
    TaskDetailView,
    TaskRelatedView,
)

urlpatterns = [
    path('user/register/', RegisterView.as_view(), name='registration'),
    path('user/login/',
         jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('user/token/refresh/',
         jwt_views.TokenRefreshView.as_view(), name='refresh_token'),

    path('tasks/', TaskCreateView.as_view(), name='tasks_create'),
    path('tasks/related/', TaskRelatedView.as_view(), name='tasks_related'),
    path('tasks/all/', TaskAllView.as_view(), name='tasks_all'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]
