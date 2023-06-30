from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from user.views import CustomBackend, jwt_response_payload_handler, RegisterViewSet, UpdatePwdApi, StudentViewSet, ClazzListViewSet
from django.db.models import Q

from django.contrib.auth.hashers import make_password, check_password 
from exam.models import SubjectiveAnswer
from question.models import Choice, Fill, Judge, Subjective
from user.models import Clazz, Student
from exam.models import Exam, Paper
from question.views import ChoiceListViewSet, FillListViewSet, JudgeListViewSet, SubjectiveListViewSet, UploadSubjective
from question.serializers import ChoiceSerializer, FillSerializer, JudgeSerializer, SubjectiveSerializer
from rest_framework import status
from rest_framework.response import Response

import requests
from unittest import mock

# Create your tests here.


class ChoiceListViewSetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_users = 13
        for user_num in range(number_of_users):
            Choice.objects.create(question='问题%s' % user_num, answer_A='1', answer_B='2', answer_C='3', answer_D='4', right_answer='A', level='2')
    
    def test_get_queryset(self):
        queryset=ChoiceListViewSet()
        user1 = queryset.serializer_class
        #print(user1)
        self.assertEqual(user1, ChoiceSerializer)


class MockRequest():
    def __init__(self, data):
        self.data=data
    
class UploadSubjectiveTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_users = 13
        for user_num in range(number_of_users):
            User.objects.create(username='user%s' % user_num, password = '654321%s' % user_num,)
        Clazz.objects.create(year='2020', major='计算机', clazz='1')
        Student.objects.create(name='syq', user=User.objects.get(id=1), gender='f', clazz=Clazz.objects.get(id=1))
        Subjective.objects.create(question='问题1', answer_template='1234567答题的模板', level='2')
        Paper.objects.create(name='试卷1', score=120)
        temp = Exam.objects.create(name='测试1', exam_date='2023-1-1', major='计算机', paper=Paper.objects.get(id=1))
        temp_class = Clazz.objects.filter(id=1)
        temp.clazzs.set(temp_class) 
    
    def test_upload_subjective(self):
        view = UploadSubjective()
        data = {"exam_id": '1', "student_id": '1', "question_id": '1', "answer": 'abcdefg', "identifier": ' '}
        mockrequest = MockRequest(data)
        requests.post = mock.Mock(return_value=mockrequest)
        res = requests.post(data=data)
        result = view.post(res)
        self.assertEqual(result.data, {"message": "success"})
