from core.serializers.task import CreateTaskSerializer, TaskInfo
from core.models import Task

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class TaskCreateView(APIView):
    renderer_classes = [JSONRenderer, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = CreateTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = request.user
        task = serializer.save()
        task_info = TaskInfo(task)
        return Response(data=task_info.data, status=200)


class TaskRelatedView(generics.ListAPIView):
    queryset = Task.objects.all()
    renderer_classes = [JSONRenderer, ]
    serializer_class = TaskInfo

    def get_queryset(self, *args, **kwargs):
        return Task.objects.filter(user=self.request.user)


class TaskAllView(generics.ListAPIView):
    renderer_classes = [JSONRenderer, ]
    serializer_class = TaskInfo
    queryset = Task.objects.all()


class TaskDetailView(APIView):
    renderer_classes = [JSONRenderer, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
