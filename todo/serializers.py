from django.contrib.auth.models import User
from users.serializers import UserSerializer
from .models import Task, Status
from rest_framework import serializers


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=True)
    class Meta:
        model = Task
        fields = '__all__'
