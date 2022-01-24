from rest_framework import serializers
from .models import Board, Column, Task
from authapi.serializers import UserSerializer

class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    columns = serializers.SerializerMethodField()
    class Meta:
        model = Board
        fields = '__all__'
        
    def get_owner(self, obj):
        return UserSerializer(obj.owner).data
    
    def get_columns(self, obj):
        return ColumnSerializer(Column.objects.filter(board=obj), many=True).data
    
class CustomForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Board.objects.filter(owner=self.context['request'].user)
class ColumnSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    board = CustomForeignKey()
    class Meta:
        model = Column
        fields = ('id', 'column_title', 'priority', 'board', 'tasks')
        
    def get_tasks(self, obj):
        return TaskSerializer(Task.objects.filter(column = obj), many=True).data

class CustomForeignKeyColumn(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Column.objects.filter(board__owner=self.context['request'].user)

class TaskSerializer(serializers.ModelSerializer):
    column = CustomForeignKeyColumn()
    class Meta:
        model = Task
        fields = '__all__'