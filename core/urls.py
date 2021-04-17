from django.urls import path

from core.views.user import RegisterView, LoginView

urlpatterns = [
    path('user/register/', RegisterView.as_view(), name='registration'),
    path('user/login/', LoginView.as_view(), name='login'),
]
