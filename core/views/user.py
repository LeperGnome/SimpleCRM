from core.serializers.user import (UserRegisterSerializer, UserInfo)

from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class LoginView(APIView):
    renderer_classes = [JSONRenderer, ]

    def post(self, request):
        """
        Acc: Public
        Des: User authentication
        """
        pass


class RegisterView(APIView):
    renderer_classes = [JSONRenderer, ]

    def post(self, request):
        """
        Acc: Public
        Des: User registration
        """
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        user_info = UserInfo(user)
        return Response(data=user_info.data, status=200)
