from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ['id', 'task', 'done', 'created_at']