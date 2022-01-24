from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Board, Column, Task
from .serializers import BoardSerializer, ColumnSerializer, TaskSerializer, CustomForeignKey, CustomForeignKeyColumn


# Create your tests here.
class Test_Board(TestCase):
    
    @classmethod
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.board = Board.objects.create(name="test", title="test", owner=self.user)

    
    def test_string_method(self):
        board = Board.objects.get(id =1)
        expected_string = f"{board.name}"
        self.assertEqual(str(board), expected_string)
        
        
class Test_Column(TestCase):
    
    @classmethod
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.board = Board.objects.create(name="test", title="test", owner=self.user)
        self.column = Column.objects.create(column_title="test", priority="0", board=self.board)

    
    def test_string_method(self):
        column = Column.objects.get(column_title ="test")
        expected_string = f"{column.board.name}" + ": " + f"{column.column_title}"
        self.assertEqual(str(column), expected_string)
        
class Test_Task(TestCase):
        
        @classmethod
        def setUp(self):
            self.user = User.objects.create_user(username="test", password="test")
            self.board = Board.objects.create(name="test", title="test", owner=self.user)
            self.column = Column.objects.create(column_title="test", priority="0", board=self.board)
            self.task = Task.objects.create(title="test", description="test", column=self.column, status=0)
    
        
        def test_string_method(self):
            task = Task.objects.get(title = "test")
            expected_string = f"{task.title}"
            self.assertEqual(str(task), expected_string)


class Test_BoardSerializer(TestCase):
    
    @classmethod
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.board = Board.objects.create(name="test", title="test", owner=self.user)
        self.column = Column.objects.create(column_title="test", priority="0", board=self.board)
        self.serializer = BoardSerializer(instance= self.board)
    
    
    def test_get_owner(self):
        self.assertEqual(self.serializer.data['owner']['username'], self.user.username)
     
    def test_get_columns(self):
        self.assertEqual(self.serializer.data['columns'][0]['column_title'], self.column.column_title)
    
class Test_ColumnSerializer(TestCase):
    
    @classmethod
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.board = Board.objects.create(name="test", title="test", owner=self.user)
        self.column = Column.objects.create(column_title="test", priority="0", board=self.board)
        self.task = Task.objects.create(title="test", description="test", column=self.column, status=0)
     
    def test_get_task(self):
        self.assertEqual(self.column.tasks.all()[0].title, "test")   
        
        
class Test_BoardViewSet(APITestCase):
    
    @classmethod
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        
    def test_perform_create(self):
        data = {"name": "test", "title": "test"}
        self.client.force_authenticate(user=self.user)
        response= self.client.post('/api/boards/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_query_set(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/boards/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

class Test_ColumnViewSet(APITestCase):
    
    @classmethod
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        
    def test_get_query_set(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/columns/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

class Test_TaskViewSet(APITestCase):
    
    @classmethod
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        
    def test_get_query_set(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        