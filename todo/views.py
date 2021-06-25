from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Task, Status
from .serializers import TaskSerializer, StatusSerializer
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions

# Create your views here.

class StatusList(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

# class StatusAct(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

class TaskView(viewsets.ViewSet):
    def list(self, request):
        queryset = Task.objects.all()
        serializers = TaskSerializer(queryset, many=True)
        return Response(serializers.data)

    def retrieve(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    

    def update(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
            
        serializer = TaskSerializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
    def destroy(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        task.delete()
        return Response({'message': 'the task has been successfully deleted'})
    
    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_all_task_user(self, request, id_user=None):
        try:
            user = User.objects.get(pk=id_user)
            tasks = Task.objects.filter(user=user.id)
            serializer = TaskSerializer(tasks, many=True)
            Response(serializer.data)
        except User.DoesNotExist:
            return Response({'message': 'this user not found'},status=status.HTTP_404_NOT_FOUND)    

    def get_all_task_state(self, request, name_state=None):
        try:
            name_state = name_state.lower()
            status = Status.objects.get(name=name_state)
            tasks = Task.objects.filter(state=status.id)
            serializer = TaskSerializer(tasks, many=True)
            Response(serializer.data)
        except Status.DoesNotExist:
            return Response({'message': 'this state not found'},status=status.HTTP_404_NOT_FOUND)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action != '':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]