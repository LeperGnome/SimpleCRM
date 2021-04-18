from core.serializers.user import (UserRegisterSerializer, UserInfo)

from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema


class RegisterView(APIView):
    renderer_classes = [JSONRenderer, ]

    @swagger_auto_schema(request_body=UserRegisterSerializer, responses={200: UserInfo})
    def post(self, request):
        """ Register new user """
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        user_info = UserInfo(user)
        return Response(data=user_info.data, status=200)
