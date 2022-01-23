from boards.models import Board, Column, Task
from rest_framework import viewsets, permissions
from .custompermissions import isOwner
from .serializers import BoardSerializer, ColumnSerializer, TaskSerializer


#Board ViewSet

class BoardViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    
    def get_queryset(self):
        return self.request.user.boards.all()
    
    
    serializer_class = BoardSerializer
    ordering = ['-created_at'] 
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
        
class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ColumnSerializer
    
    def get_queryset(self):
        return  super().get_queryset().filter(board__owner=self.request.user)
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = TaskSerializer
    
    
    def get_queryset(self):
        return  super().get_queryset().filter(column__board__owner=self.request.user)
