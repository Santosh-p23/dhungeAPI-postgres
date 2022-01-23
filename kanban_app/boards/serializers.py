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
    
class ColumnSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    class Meta:
        model = Column
        fields = '__all__'
        
    def get_tasks(self, obj):
        return TaskSerializer(Task.objects.filter(column = obj), many=True).data


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'