from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from exam.models import SubjectiveAnswer
from question.models import Choice, Fill, Judge, Subjective
from user.models import Clazz, Student
from exam.models import Exam, Paper
from exam.views import CommonPagination, ExamListViewSet
from exam.serializers import ExamSerializer
from rest_framework import status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

import requests
from unittest import mock

# Create your tests here.


class CommonPaginationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_users = 13
        for user_num in range(number_of_users):
            Choice.objects.create(question='问题%s' % user_num, answer_A='1', answer_B='2', answer_C='3', answer_D='4', right_answer='A', level='2')
    
    def test_set_page(self):
        pageset=CommonPagination()
        user1 = pageset.page_size
        self.assertEqual(user1, 10)
        user2 = pageset.page_size_query_param
        self.assertEqual(user2, 'page_size')

    
class ExamListViewSetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_users = 13
        for user_num in range(number_of_users):
            Choice.objects.create(question='问题%s' % user_num, answer_A='1', answer_B='2', answer_C='3', answer_D='4', right_answer='A', level='2')
    
    def test_get_queryset(self):
        queryset=ExamListViewSet()
        user1 = queryset.serializer_class
        self.assertEqual(user1, ExamSerializer)
        user2 = queryset.pagination_class
        self.assertEqual(user2, CommonPagination)
        user3 = queryset.filter_backends
        self.assertEqual(user3, (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter))
