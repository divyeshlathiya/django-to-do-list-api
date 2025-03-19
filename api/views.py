from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializers
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

