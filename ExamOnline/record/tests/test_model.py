from django.test import TestCase
#from index.models import User
from exam.models import Practice
from question.models import Choice, Fill, Judge, Subjective
from user.models import Student, Clazz
from record.models import Record, ChoiceRecord, FillRecord, JudgeRecord, SubjectiveRecord
from django.contrib.auth.models import User

# Create your tests here.
# Record类是抽象类，不用测试

class ChoiceRecordModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Clazz.objects.create(year='2020', major='计算机', clazz='1')
        User.objects.create(username='user0', password = '6543210')
        Student.objects.create(name='张三', user=User.objects.get(id=1), gender='m', clazz=Clazz.objects.get(id=1))
        Practice.objects.create(name='练习1', student=Student.objects.get(id=1), create_time=2023/1/1)
        Choice.objects.create(question='问题1', answer_A='1', answer_B='2', answer_C='3', answer_D='4', right_answer='A', level='2')
        ChoiceRecord.objects.create(practice=Practice.objects.get(id=1), student=Student.objects.get(id=1), your_answer='1', choice=Choice.objects.get(id=1))

    def test_practice_label(self):
        record=ChoiceRecord.objects.get(id=1)
        field_label = record._meta.get_field('practice').verbose_name
        self.assertEquals(field_label,"练习")

    def test_student_label(self):
        record=ChoiceRecord.objects.get(id=1)
        field_label = record._meta.get_field('student').verbose_name
        self.assertEquals(field_label,"学生")

    def test_your_answer_label(self):
        record=ChoiceRecord.objects.get(id=1)
        field_label = record._meta.get_field('your_answer').verbose_name
        self.assertEquals(field_label,"你的作答")

    def test_choice_label(self):
        record=ChoiceRecord.objects.get(id=1)
        field_label = record._meta.get_field('choice').verbose_name
        self.assertEquals(field_label,"选择题")

    def test_object_name(self):
        record=ChoiceRecord.objects.get(id=1)
        expected_object_name = '%s' % (record.your_answer)
        self.assertEquals(expected_object_name,str(record))


class FillRecordModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Clazz.objects.create(year='2020', major='计算机', clazz='1')
        User.objects.create(username='user0', password = '6543210')
        Student.objects.create(name='张三', user=User.objects.get(id=1), gender='m', clazz=Clazz.objects.get(id=1))
        Practice.objects.create(name='练习1', student=Student.objects.get(id=1), create_time=2023/1/1)
        Fill.objects.create(question='问题1', right_answer='A', level='2')
        FillRecord.objects.create(practice=Practice.objects.get(id=1), student=Student.objects.get(id=1), your_answer='1', fill=Fill.objects.get(id=1))

    def test_practice_label(self):
        record=FillRecord.objects.get(id=1)
        field_label = record._meta.get_field('practice').verbose_name
        self.assertEquals(field_label,"练习")

    def test_student_label(self):
        record=FillRecord.objects.get(id=1)
        field_label = record._meta.get_field('student').verbose_name
        self.assertEquals(field_label,"学生")

    def test_your_answer_label(self):
        record=FillRecord.objects.get(id=1)
        field_label = record._meta.get_field('your_answer').verbose_name
        self.assertEquals(field_label,"你的作答")

    def test_fill_label(self):
        record=FillRecord.objects.get(id=1)
        field_label = record._meta.get_field('fill').verbose_name
        self.assertEquals(field_label,"填空题")

    def test_object_name(self):
        record=FillRecord.objects.get(id=1)
        expected_object_name = '%s' % (record.your_answer)
        self.assertEquals(expected_object_name,str(record))


class SubjectiveRecordModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Clazz.objects.create(year='2020', major='计算机', clazz='1')
        User.objects.create(username='user0', password = '6543210')
        Student.objects.create(name='张三', user=User.objects.get(id=1), gender='m', clazz=Clazz.objects.get(id=1))
        Practice.objects.create(name='练习1', student=Student.objects.get(id=1), create_time=2023/1/1)
        Subjective.objects.create(question='问题1', answer_template='1234567答题的模板', level='2')
        SubjectiveRecord.objects.create(practice=Practice.objects.get(id=1), student=Student.objects.get(id=1), your_answer='1', program=Subjective.objects.get(id=1), cmd_msg='cmd_msg')

    def test_practice_label(self):
        record=SubjectiveRecord.objects.get(id=1)
        field_label = record._meta.get_field('practice').verbose_name
        self.assertEquals(field_label,"练习")

    def test_student_label(self):
        record=SubjectiveRecord.objects.get(id=1)
        field_label = record._meta.get_field('student').verbose_name
        self.assertEquals(field_label,"学生")

    def test_your_answer_label(self):
        record=SubjectiveRecord.objects.get(id=1)
        field_label = record._meta.get_field('your_answer').verbose_name
        self.assertEquals(field_label,"你的作答")

    def test_program_label(self):
        record=SubjectiveRecord.objects.get(id=1)
        field_label = record._meta.get_field('program').verbose_name
        self.assertEquals(field_label,"主观题")

    def test_cmd_msg_label(self):
        record=SubjectiveRecord.objects.get(id=1)
        field_label = record._meta.get_field('cmd_msg').verbose_name
        self.assertEquals(field_label,"输出结果")

    def test_object_name(self):
        record=SubjectiveRecord.objects.get(id=1)
        expected_object_name = '%s' % (record.your_answer)
        self.assertEquals(expected_object_name,str(record))