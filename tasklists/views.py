from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from tasklists.models import TaskList, Task

from tasklists.serializers import TaskListSerializer, TaskListSerializerFull, TaskSerializer



class TaskListViewSet(ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    serializer_class = TaskListSerializer
    queryset = TaskList.objects.all()

    # Para que sólo salgan las listas del usuario logueado
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    # Sobreesribiimos el método perform_create para que al crear listas, se ponga como propietario el usuario que hace la acción.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskListSerializerFull
        else:
            return self.serializer_class

class TaskViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()