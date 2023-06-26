from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets

from question.models import Subjective
from record.models import ChoiceRecord, FillRecord, JudgeRecord, SubjectiveRecord
from record.serializers import ChoiceRecordSerializer, FillRecordSerializer, JudgeRecordSerializer, \
    SubjectiveRecordSerializer


class ChoiceRecordListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """选择题练习记录"""
    # 数据集
    queryset = ChoiceRecord.objects.all()
    # 序列化
    serializer_class = ChoiceRecordSerializer

    def get_queryset(self):
        # 模拟练习ID
        practice_id = self.request.query_params.get('practice_id')
        if practice_id:
            self.queryset = ChoiceRecord.objects.filter(practice_id=practice_id)
        return self.queryset


class FillRecordListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """填空题练习记录"""
    # 数据集
    queryset = FillRecord.objects.all()
    # 序列化
    serializer_class = FillRecordSerializer

    def get_queryset(self):
        # 模拟练习ID
        practice_id = self.request.query_params.get('practice_id')
        if practice_id:
            self.queryset = FillRecord.objects.filter(practice_id=practice_id)
        return self.queryset


class JudgeRecordListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """选择题练习记录"""
    # 数据集
    queryset = JudgeRecord.objects.all()
    # 序列化
    serializer_class = JudgeRecordSerializer

    def get_queryset(self):
        # 模拟练习ID
        practice_id = self.request.query_params.get('practice_id')
        if practice_id:
            self.queryset = JudgeRecord.objects.filter(practice_id=practice_id)
        return self.queryset


class SubjectiveRecordListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """主观题练习记录"""
    # 数据集
    queryset = SubjectiveRecord.objects.all()
    # 序列化
    serializer_class = SubjectiveRecordSerializer

    def get_queryset(self):
        # 模拟练习ID
        practice_id = self.request.query_params.get('practice_id')
        if practice_id:
            self.queryset = SubjectiveRecord.objects.filter(practice_id=practice_id)
        return self.queryset
