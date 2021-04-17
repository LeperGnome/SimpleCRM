from rest_framework import serializers
from core.models import Task


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description', 'deadline_at']
        read_only_fields = ['id', 'created_at']


class TaskInfo(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
