from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer


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
        pass
