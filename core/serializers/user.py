from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        obj = User.objects.create_user(**validated_data)
        return obj

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']


class UserInfo(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id', 'first_name',
                  'last_name', 'date_joined']
