from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from user.views import CustomBackend, jwt_response_payload_handler, RegisterViewSet, UpdatePwdApi, StudentViewSet, ClazzListViewSet
from django.db.models import Q

from django.contrib.auth.hashers import make_password, check_password 
from user.models import Student, Clazz
from user.serializers import StudentSerializer, UserDetailSerializer, ClazzSerializer
from rest_framework import status
from rest_framework.response import Response

import requests
from unittest import mock

# Create your tests here.


class CustomBackendTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_users = 13
        for user_num in range(number_of_users):
            User.objects.create(username='user%s' % user_num, password = '654321%s' % user_num,)
        Clazz.objects.create(year='2020', major='计算机', clazz='1')
        Student.objects.create(name='syq', user=User.objects.get(id=1), gender='f', clazz=Clazz.objects.get(id=1))
    
    def test_authenticate(self):
        backend=CustomBackend()
        user1 = backend.authenticate(username='user0', password = '6543210')
        #user1 = User.objects.get(Q(username='user0') | Q(mobile='user0'))
        #if check_password('6543210', make_password('6543210')):
        #    self.assertEqual(0, 1)
        self.assertEqual(user1, User.objects.get(id=1))

    def test_authenticate_fail(self):
        backend=CustomBackend()
        user1 = backend.authenticate(username='user0', password = '654321')
        #user1 = User.objects.get(Q(username='user0') | Q(mobile='user0'))
        #if check_password('6543210', make_password('6543210')):
        #    self.assertEqual(0, 1)
        self.assertEqual(user1, None)

    def test_jwt_response_payload_handler(self):
        token = '1'
        user = User.objects.get(id=1)
        result = jwt_response_payload_handler(token=token, user=user)
        expect = {
            'token': token,
            'user': UserDetailSerializer(user, context={'request': None}).data,
            'student': StudentSerializer(Student.objects.get(id=1), context={'request': None}).data
        }

        self.assertEqual(result, expect)

class MockRequest():
    def __init__(self, data):
        self.data=data

class RegisterViewSetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_users = 13
        for user_num in range(number_of_users):
            User.objects.create(username='user%s' % user_num, password = '654321%s' % user_num,)
        Clazz.objects.create(year='2020', major='计算机', clazz='1')
        Student.objects.create(name='syq', user=User.objects.get(id=1), gender='f', clazz=Clazz.objects.get(id=1))
    
    def test_create_user_fail(self):
        view = RegisterViewSet()
        data = {'username': 'user2', 'name': 'abc'}
        url = "localhost:8000/register"
        mockrequest = MockRequest(data)
        requests.post = mock.Mock(return_value=mockrequest)
        res = requests.post(url, data=data)
        result = view.create(res)
        self.assertEqual(result.status_code, 201)
    
    def test_create_user(self):
        view = RegisterViewSet()
        data = {'username': 'user14', 'name': 'abc', 'password': 123456}
        url = "localhost:8000/register"
        mockrequest = MockRequest(data)
        requests.post = mock.Mock(return_value=mockrequest)
        res = requests.post(url, data=data)
        result = view.create(res)
        #user_detail = UserDetailSerializer(data=request.data)
        self.assertEqual(result.status_code, 200)
    
class UpdatePwdApiTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_users = 13
        for user_num in range(number_of_users):
            User.objects.create(username='user%s' % user_num, password = '654321%s' % user_num,)
        Clazz.objects.create(year='2020', major='计算机', clazz='1')
        Student.objects.create(name='syq', user=User.objects.get(id=1), gender='f', clazz=Clazz.objects.get(id=1))
    
    def test_update_pwd_fail(self):
        view = UpdatePwdApi()
        data = {'userid': '2', 'oldpwd': '654321', 'newpwd': '6543212'}
        mockrequest = MockRequest(data)
        requests.post = mock.Mock(return_value=mockrequest)
        res = requests.post(data=data)
        result = view.patch(res)
        self.assertEqual(result.data, {'msg': 'fail'})
    
    def test_update_pwd(self):
        view = UpdatePwdApi()
        data = {'userid': '2', 'oldpwd': '6543211', 'newpwd': '654321'}
        mockrequest = MockRequest(data)
        requests.post = mock.Mock(return_value=mockrequest)
        res = requests.post(data=data)
        result = view.patch(res)
        self.assertEqual(result.data, {'msg': 'success'})


class StudentViewSetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_users = 13
        for user_num in range(number_of_users):
            User.objects.create(username='user%s' % user_num, password = '654321%s' % user_num,)
        Clazz.objects.create(year='2020', major='计算机', clazz='1')
        for user_num in range(number_of_users):
            Student.objects.create(name='syq', user=User.objects.get(id=user_num+1), gender='f', clazz=Clazz.objects.get(id=1))
    
    def test_view_url_exists(self):
        resp = self.client.get('/students', follow=True)
        self.assertEqual(resp.status_code, 200)
    
    def test_lists_all_students(self):
        resp = self.client.get('/students', follow=True)
        self.assertEqual(resp.status_code, 200)
        number_of_users = 13
        for user_num in range(number_of_users):
            self.assertEqual(resp.data[user_num]['id'],user_num+1)
            self.assertEqual(resp.data[user_num]['user'],user_num+1)
        
class ClazzListViewSetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_users = 13
        for user_num in range(number_of_users):
            User.objects.create(username='user%s' % user_num, password = '654321%s' % user_num,)
            Clazz.objects.create(year='2020', major='计算机', clazz='1%s' % user_num,)
        
    
    def test_view_url_exists(self):
        resp = self.client.get('/clazzs', follow=True)
        self.assertEqual(resp.status_code, 200)
    
    def test_lists_all_clazz(self):
        resp = self.client.get('/clazzs', follow=True)
        self.assertEqual(resp.status_code, 200)
        number_of_users = 13
        for user_num in range(number_of_users):
            self.assertEqual(resp.data[user_num]['id'], user_num+1)
            self.assertEqual(resp.data[user_num]['clazz'], str(1)+str(user_num))
    

