from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from core.views.user import RegisterView

urlpatterns = [
    path('user/register/', RegisterView.as_view(), name='registration'),
    path('user/login/',
         jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('user/token/refresh/',
         jwt_views.TokenRefreshView.as_view(), name='refresh_token'),
]
