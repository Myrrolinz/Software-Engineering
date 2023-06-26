import subprocess

from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from exam.models import SubjectiveAnswer
from question.models import Choice, Fill, Judge, Subjective
from question.serializers import ChoiceSerializer, FillSerializer, JudgeSerializer, SubjectiveSerializer


# Create your views here.


class ChoiceListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """选择题列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Choice.objects.all().order_by('id')[:0]
    # 序列化
    serializer_class = ChoiceSerializer

    # 重写queryset
    def get_queryset(self):
        # 题目数量
        choice_number = int(self.request.query_params.get("choice_number"))
        level = int(self.request.query_params.get("level", 1))

        if choice_number:
            self.queryset = Choice.objects.all().filter(level=level).order_by('?')[:choice_number]
        return self.queryset


class FillListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """填空题列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Fill.objects.all().order_by('id')[:0]
    # 序列化
    serializer_class = FillSerializer

    # 重写queryset
    def get_queryset(self):
        # 题目数量
        fill_number = int(self.request.query_params.get("fill_number"))
        level = int(self.request.query_params.get("level", 1))

        if fill_number:
            self.queryset = Fill.objects.all().filter(level=level).order_by('?')[:fill_number]
        return self.queryset


class JudgeListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """判断题列表页"""
    # 这里要定义一个默认的排序，否则会报错
    queryset = Judge.objects.all().order_by('?')[:0]
    # 序列化
    serializer_class = JudgeSerializer

    # 重写queryset
    def get_queryset(self):
        # 题目数量
        judge_number = int(self.request.query_params.get("judge_number"))
        level = int(self.request.query_params.get("level", 1))

        if judge_number:
            self.queryset = Judge.objects.all().filter(level=level).order_by('?')[:judge_number]
        return self.queryset


class SubjectiveListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """主观题列表页"""
    # 这里定义一个默认的排序，否则会报错
    queryset = Subjective.objects.all().order_by('?')[:0]
    # 序列化
    serializer_class = SubjectiveSerializer

    # 重写queryset
    def get_queryset(self):
        # 题目数量
        subjective_number = int(self.request.query_params.get("subjective_number"))
        level = int(self.request.query_params.get("level", 1))

        if subjective_number:
            self.queryset = Subjective.objects.all().filter(level=level).order_by('?')[:subjective_number]
        return self.queryset


class UploadSubjective(APIView):
    """上传主观题答案"""

    def post(self, request):
        # 获取post提交的字典数据
        json_body = request.data
        # 获取题目信息
        exam_id = json_body.get("exam_id")
        student_id = json_body.get("student_id")
        question_id = json_body.get("question_id")
        answer = json_body.get("answer")
        identifier = json_body.get("identifier")
        # 把id和answer存入数据库Subjective
        SubjectiveAnswer.objects.create(student_id=student_id, question_id=question_id, answer=answer, exam_id=exam_id,identifier=identifier)
        return Response({"message": "success"})
