from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, filters
from rest_framework.pagination import PageNumberPagination

from exam.filter import ExamFilter
from exam.models import Exam, Grade, Practice, SubjectiveAnswer
from exam.serializers import ExamSerializer, GradeSerializer, PracticeSerializer, SubjectiveSerializer
# Create your views here.
from user.models import Student


class CommonPagination(PageNumberPagination):
    """考试列表自定义分页"""
    # 默认每页显示的个数
    page_size = 10
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 10


class ExamListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """考试列表页"""
    # 这里必须要定义一个默认的排序,否则会报错
    queryset = Exam.objects.all().order_by('id')
    # 序列化
    serializer_class = ExamSerializer
    # 分页
    pagination_class = CommonPagination
    # 开启过滤
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 设置filter的类为我们自定义的类
    filter_class = ExamFilter
    # 搜索,=name表示精确搜索，也可以使用各种正则表达式
    search_fields = ('name', 'major')
    # 排序
    ordering_fields = ('id', 'exam_date')

    # 重写queryset
    def get_queryset(self):
        # 学生ID
        student_id = self.request.query_params.get("student_id")
        student = Student.objects.get(id=student_id)

        if student:
            self.queryset = Exam.objects.filter(clazzs__student=student)
        return self.queryset


class GradeListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """成绩列表"""
    # 这里必须要定义一个默认的排序,否则会报错
    queryset = Grade.objects.all().order_by('-create_time')
    # 序列化
    serializer_class = GradeSerializer
    # 分页
    pagination_class = CommonPagination

    # 重写queryset
    def get_queryset(self):
        # 学生ID
        student_id = self.request.query_params.get("student_id")

        if student_id:
            self.queryset = Grade.objects.filter(student_id=student_id)
        # 修改分数的数值
        for grade in self.queryset:
            # 查找所有Subjective表中，student_id=student_id,exam_id = grade.exam_id的数据
            subjective_list: list = SubjectiveAnswer.objects.filter(student_id=student_id, exam_id=grade.exam_id, identifier=grade.identifier)
            # 如果有数据，就把分数相加 
            if subjective_list:
                score = grade.score
                for subjective in subjective_list:
                    score += subjective.score if subjective.score else 0
                grade.score = score

        return self.queryset


class PracticeListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """练习列表"""
    # 数据集 
    queryset = Practice.objects.all()
    # 序列化 
    serializer_class = PracticeSerializer
    # 分页 
    pagination_class = CommonPagination

    def get_queryset(self):
        # 学生ID 
        student_id = self.request.query_params.get('student_id')
        if student_id:
            self.queryset = Practice.objects.filter(student_id=student_id)
        return self.queryset


class SubjectiveListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """主观题列表"""
    # 数据集，需要排除已经批改（就是有分数的）的主观题 
    queryset = SubjectiveAnswer.objects.filter()
    # 序列化 
    serializer_class = SubjectiveSerializer
    # 分页 
    pagination_class = CommonPagination

    def get_queryset(self):
        # 学生ID
        student_id = self.request.query_params.get('student_id')
        if student_id:
            self.queryset = SubjectiveAnswer.objects.filter(student_id=student_id)
        self.queryset = self.queryset.order_by(F('score').asc(nulls_first=True))
        return self.queryset
