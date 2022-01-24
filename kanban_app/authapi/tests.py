from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.


class Test_LoginView(APITestCase):
    @classmethod
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
    
    def test_login_view(self):
        data = "{\"username\": \"test\", \"password\": \"test\"}"
        response = self.client.generic('POST','/login/',data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_login_view_wrong_password(self):
        data = "{\"username\": \"test\", \"password\": \"wrong\"}"
        response = self.client.generic('POST','/login/',data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
       
        
    def test_login_view_wrong_username(self):
        data = "{\"username\": \"wrong\", \"password\": \"test\"}"
        response = self.client.generic('POST','/login/',data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_login_view_wrong_username_and_password(self):
        data = "{\"username\": \"wrong\", \"password\": \"wrong\"}"
        response = self.client.generic('POST','/login/',data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_login_view_no_username(self):
        data = "{\"password\": \"test\"}"
        response = self.client.generic('POST','/login/',data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_login_view_no_password(self):
        data = "{\"username\": \"test\"}"
        response = self.client.generic('POST','/login/',data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_login_view_no_username_and_password(self):
        data = "{}"
        response = self.client.generic('POST','/login/',data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        


class Test_LogoutView(APITestCase):
    
    @classmethod
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        
    def test_logout(self):
        data = {'username': 'test', 'password': 'test'}
        self.client.force_login(User.objects.get_or_create(username='test')[0])
        response= self.client.post('/logout/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_unauthenticated_logout_view(self):
        response = self.client.generic('POST','/logout/',{})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        

class Test_RegisterView(APITestCase):
     
    def test_register_view(self):
        data = "{\"username\": \"test\", \"password\": \"test\", \"email\": \"test@test.com\"}"
        response = self.client.generic('POST','/register/',data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_register_view_no_username(self):
        data = "{\"password\": \"test\", \"email\": \"test@test.com\"}"
        response = self.client.generic('POST','/register/',data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        