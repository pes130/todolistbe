from rest_framework import serializers
from tasklists.models import TaskList, Task


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskList
        fields = ['id', 'name', 'description', 'creation_date']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description','completed','list'] 


class TaskListSerializerFull(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = TaskList
        fields = ['id', 'name', 'description', 'creation_date', 'tasks']

