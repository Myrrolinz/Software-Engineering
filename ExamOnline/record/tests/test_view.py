from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from exam.models import SubjectiveAnswer
from question.models import Choice, Fill, Judge, Subjective
from user.models import Clazz, Student
from exam.models import Exam, Paper
from record.models import ChoiceRecord, FillRecord, JudgeRecord, SubjectiveRecord
from record.views import ChoiceRecordListViewSet, FillRecordListViewSet, JudgeRecordListViewSet, SubjectiveRecordListViewSet
from record.serializers import ChoiceRecordSerializer, FillRecordSerializer, JudgeRecordSerializer, SubjectiveRecordSerializer
from rest_framework import status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

import requests
from unittest import mock

# Create your tests here.    
class ChoiceRecordListViewSetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        queryset=ChoiceRecordListViewSet()

    def test_get_queryset(self):
        queryset=ChoiceRecordListViewSet()
        user1 = queryset.serializer_class
        self.assertEqual(user1, ChoiceRecordSerializer)

class FillRecordListViewSetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        queryset=FillRecordListViewSet()

    def test_get_queryset(self):
        queryset=FillRecordListViewSet()
        user1 = queryset.serializer_class
        self.assertEqual(user1, FillRecordSerializer)

class JudgeRecordListViewSetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        queryset=JudgeRecordListViewSet()

    def test_get_queryset(self):
        queryset=JudgeRecordListViewSet()
        user1 = queryset.serializer_class
        self.assertEqual(user1, JudgeRecordSerializer)

class SubjectiveRecordListViewSetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        queryset=SubjectiveRecordListViewSet()

    def test_get_queryset(self):
        queryset=SubjectiveRecordListViewSet()
        user1 = queryset.serializer_class
        self.assertEqual(user1, SubjectiveRecordSerializer)
