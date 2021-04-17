from core.serializers.task import TaskSerializer, TaskInfo
from core.models import Task

from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class TaskCreateView(APIView):
    renderer_classes = [JSONRenderer, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
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

    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task_info = TaskInfo(task)
        return Response(data=task_info.data, status=200)

    def put(self, request, pk):
        task = get_object_or_404(Task,id=pk, user=request.user)
        serializer = TaskSerializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_task = serializer.save()
        task_info = TaskInfo(updated_task)
        return Response(data=task_info.data, status=200)


    def delete(self, request, pk):
        task = get_object_or_404(Task, id=pk, user=request.user)
        task.delete()
        return Response(data={"detail": "Successfully deleted"}, status=200)
