from tasks.models import Task
from rest_framework import viewsets, permissions
from tasks.serializers import TaskSerializer, TaskFilter

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer
    filterset_class = TaskFilter