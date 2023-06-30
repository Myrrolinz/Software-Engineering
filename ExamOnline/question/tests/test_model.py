from django.test import TestCase
#from index.models import User
from exam.models import Practice
from question.models import Choice, Fill, Judge, Subjective
from user.models import Student, Clazz
from question.models import Choice, Fill, Judge, Subjective
from django.contrib.auth.models import User

# Create your tests here.

class ChoiceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Choice.objects.create(question='问题1', answer_A='1', answer_B='2', answer_C='3', answer_D='4', right_answer='A', level='2')

    def test_question_label(self):
        choice=Choice.objects.get(id=1)
        field_label = choice._meta.get_field('question').verbose_name
        self.assertEquals(field_label,"题目")

    def test_answer_A_label(self):
        choice=Choice.objects.get(id=1)
        field_label = choice._meta.get_field('answer_A').verbose_name
        self.assertEquals(field_label,"A选项")

    def test_answer_B_label(self):
        choice=Choice.objects.get(id=1)
        field_label = choice._meta.get_field('answer_B').verbose_name
        self.assertEquals(field_label,"B选项")
    
    def test_answer_C_label(self):
        choice=Choice.objects.get(id=1)
        field_label = choice._meta.get_field('answer_C').verbose_name
        self.assertEquals(field_label,"C选项")

    def test_answer_D_label(self):
        choice=Choice.objects.get(id=1)
        field_label = choice._meta.get_field('answer_D').verbose_name
        self.assertEquals(field_label,"D选项")

    def test_right_answer_label(self):
        choice=Choice.objects.get(id=1)
        field_label = choice._meta.get_field('right_answer').verbose_name
        self.assertEquals(field_label,"正确选项")

    def test_analysis_label(self):
        choice=Choice.objects.get(id=1)
        field_label = choice._meta.get_field('analysis').verbose_name
        self.assertEquals(field_label,"题目解析")

    def test_score_label(self):
        choice=Choice.objects.get(id=1)
        field_label = choice._meta.get_field('score').verbose_name
        self.assertEquals(field_label,"分值")

    def test_level_label(self):
        choice=Choice.objects.get(id=1)
        field_label = choice._meta.get_field('level').verbose_name
        self.assertEquals(field_label,"难度等级")

    def test_right_answer_max_length(self):
        choice=Choice.objects.get(id=1)
        max_length = choice._meta.get_field('right_answer').max_length
        self.assertEquals(max_length,1)

    def test_answer_A_max_length(self):
        choice=Choice.objects.get(id=1)
        max_length = choice._meta.get_field('answer_A').max_length
        self.assertEquals(max_length,200)

    def test_answer_B_max_length(self):
        choice=Choice.objects.get(id=1)
        max_length = choice._meta.get_field('answer_B').max_length
        self.assertEquals(max_length,200)

    def test_answer_C_max_length(self):
        choice=Choice.objects.get(id=1)
        max_length = choice._meta.get_field('answer_C').max_length
        self.assertEquals(max_length,200)

    def test_answer_D_max_length(self):
        choice=Choice.objects.get(id=1)
        max_length = choice._meta.get_field('answer_D').max_length
        self.assertEquals(max_length,200)

    def test_level_max_length(self):
        choice=Choice.objects.get(id=1)
        max_length = choice._meta.get_field('level').max_length
        self.assertEquals(max_length,1)

    def test_object_name(self):
        choice=Choice.objects.get(id=1)
        expected_object_name = '%s' % (choice.question)
        self.assertEquals(expected_object_name,str(choice))


class FillModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Fill.objects.create(question='问题1', right_answer='A', level='2')

    def test_question_label(self):
        fill=Fill.objects.get(id=1)
        field_label = fill._meta.get_field('question').verbose_name
        self.assertEquals(field_label,"题目")

    def test_right_answer_label(self):
        fill=Fill.objects.get(id=1)
        field_label = fill._meta.get_field('right_answer').verbose_name
        self.assertEquals(field_label,"正确答案")

    def test_analysis_label(self):
        fill=Fill.objects.get(id=1)
        field_label = fill._meta.get_field('analysis').verbose_name
        self.assertEquals(field_label,"题目解析")

    def test_score_label(self):
        fill=Fill.objects.get(id=1)
        field_label = fill._meta.get_field('score').verbose_name
        self.assertEquals(field_label,"分值")

    def test_level_label(self):
        fill=Fill.objects.get(id=1)
        field_label = fill._meta.get_field('level').verbose_name
        self.assertEquals(field_label,"难度等级")

    def test_right_answer_max_length(self):
        fill=Fill.objects.get(id=1)
        max_length = fill._meta.get_field('right_answer').max_length
        self.assertEquals(max_length,200)

    def test_level_max_length(self):
        fill=Fill.objects.get(id=1)
        max_length = fill._meta.get_field('level').max_length
        self.assertEquals(max_length,1)

    def test_object_name(self):
        fill=Fill.objects.get(id=1)
        expected_object_name = '%s' % (fill.question)
        self.assertEquals(expected_object_name,str(fill))


#TODO:Judge暂时没写  四六级里有判断题吗？ 


class SubjectiveModelTest(TestCase):
    """班级模型测试"""

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Subjective.objects.create(question='问题1', answer_template='1234567答题的模板', level='2')

    def test_question_label(self):
        subjective=Subjective.objects.get(id=1)
        field_label = subjective._meta.get_field('question').verbose_name
        self.assertEquals(field_label,"题目")

    def test_answer_template_label(self):
        subjective=Subjective.objects.get(id=1)
        field_label = subjective._meta.get_field('answer_template').verbose_name
        self.assertEquals(field_label,"答题模板")

    def test_analysis_label(self):
        subjective=Subjective.objects.get(id=1)
        field_label = subjective._meta.get_field('analysis').verbose_name
        self.assertEquals(field_label,"题目解析")

    def test_score_label(self):
        subjective=Subjective.objects.get(id=1)
        field_label = subjective._meta.get_field('score').verbose_name
        self.assertEquals(field_label,"分值")

    def test_level_label(self):
        subjective=Subjective.objects.get(id=1)
        field_label = subjective._meta.get_field('level').verbose_name
        self.assertEquals(field_label,"难度等级")

    def test_question_max_length(self):
        subjective=Subjective.objects.get(id=1)
        max_length = subjective._meta.get_field('question').max_length
        self.assertEquals(max_length,200)

    def test_level_max_length(self):
        subjective=Subjective.objects.get(id=1)
        max_length = subjective._meta.get_field('level').max_length
        self.assertEquals(max_length,1)

    def test_object_name(self):
        subjective=Subjective.objects.get(id=1)
        expected_object_name = '%s' % (subjective.question)
        self.assertEquals(expected_object_name,str(subjective))