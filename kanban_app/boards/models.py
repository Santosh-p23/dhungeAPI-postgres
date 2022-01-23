from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(
        User, related_name="boards", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering =('-created_at',)
        
    def __str__(self):
        return self.name
        
        
class Column(models.Model):
    options =(('0','Low'),('1','Medium'),('2','High'))
    
    column_title = models.CharField(max_length=255)
    priority = models.CharField(max_length=20, choices=options)
    board = models.ForeignKey("Board", related_name="columns", on_delete=models.CASCADE)
   
    class Meta:
        ordering = ["-priority"]

    def __str__(self):
        return f"{self.board.name}" + ": " + f"{self.column_title}"
        
        
class Task(models.Model):
    
    options = (("2", "In Progress"), ("1", "To Do"), ("0", "Done"))
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    column = models.ForeignKey("Column", related_name="tasks", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=options)
    class Meta:
        ordering = ["-status"]

    def __str__(self):
        return f"{self.title}"