from rest_framework import serializers

from exam.models import Exam, Paper, Grade, Practice,Subjective
from user.models import Student
from user.serializers import StudentSerializer


class PaperSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Paper
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    paper = PaperSerializer()

    class Meta:
        model = Exam
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    # 覆盖外键字段 只读
    exam = ExamSerializer(read_only=True)
    student = StudentSerializer(read_only=True)

    # 用于创建的只写字段
    exam_id = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all(), source='exam', write_only=True) # source 指定外键字段
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True) # source 指定外键字段

    class Meta:
        model = Grade
        fields = '__all__'


class PracticeSerializer(serializers.ModelSerializer):
    # 覆盖外键字段 只读
    student = StudentSerializer(read_only=True)

    # 用于创建的只写字段
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True)

    class Meta:
        model = Practice
        fields = '__all__'

class SubjectiveSerializer(serializers.ModelSerializer):
    # 覆盖外键字段 只读
    student = StudentSerializer(read_only=True)

    # 用于创建的只写字段
    no_score = serializers.PrimaryKeyRelatedField(
        queryset=Subjective.objects.exclude(score=None),
        source='score',
        write_only=True
    )

    class Meta:
        model = Subjective
        fields = '__all__'
        queryset = Subjective.objects.exclude(score=None)  # 添加 queryset 属性进行过滤