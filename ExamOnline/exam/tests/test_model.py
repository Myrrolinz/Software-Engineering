from django.test import TestCase
#from index.models import User
from exam.models import Practice, Paper, Exam, SubjectiveAnswer, Grade
from question.models import Choice, Fill, Judge, Subjective
from user.models import Student, Clazz
from question.models import Choice, Fill, Judge, Subjective
from django.contrib.auth.models import User

# Create your tests here.
class PaperModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Paper.objects.create(name='试卷1', score='1', choice_number='2', fill_number='3', judge_number='4', subjective_number='5', level='2')

    def test_name_label(self):
        paper=Paper.objects.get(id=1)
        field_label = paper._meta.get_field('name').verbose_name
        self.assertEquals(field_label,"试卷名称")

    def test_score_label(self):
        paper=Paper.objects.get(id=1)
        field_label = paper._meta.get_field('score').verbose_name
        self.assertEquals(field_label,"总分")

    def test_choice_number_label(self):
        paper=Paper.objects.get(id=1)
        field_label = paper._meta.get_field('choice_number').verbose_name
        self.assertEquals(field_label,"选择题数")
    
    def test_fill_number_label(self):
        paper=Paper.objects.get(id=1)
        field_label = paper._meta.get_field('fill_number').verbose_name
        self.assertEquals(field_label,"填空题数")

    def test_judge_number_label(self):
        paper=Paper.objects.get(id=1)
        field_label = paper._meta.get_field('judge_number').verbose_name
        self.assertEquals(field_label,"判断题数")

    def test_subjective_number_label(self):
        paper=Paper.objects.get(id=1)
        field_label = paper._meta.get_field('subjective_number').verbose_name
        self.assertEquals(field_label,"主观题数")

    def test_level_label(self):
        paper=Paper.objects.get(id=1)
        field_label = paper._meta.get_field('level').verbose_name
        self.assertEquals(field_label,"难度等级")

    def test_name_max_length(self):
        paper=Paper.objects.get(id=1)
        max_length = paper._meta.get_field('name').max_length
        self.assertEquals(max_length,20)

    def test_level_max_length(self):
        paper=Paper.objects.get(id=1)
        max_length = paper._meta.get_field('level').max_length
        self.assertEquals(max_length,1)

    def test_object_name(self):
        paper=Paper.objects.get(id=1)
        expected_object_name = '%s' % (paper.name)
        self.assertEquals(expected_object_name,str(paper))

    def test_save(self):
        paper=Paper.objects.get(id=1)
        paper.save()
        expected_score = (paper.choice_number + paper.fill_number + paper.judge_number) * 2 + paper.subjective_number * 8
        self.assertEquals(expected_score,paper.score)


class ExamModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Paper.objects.create(name='试卷1', score=120)
        temp = Exam.objects.create(name='测试1', exam_date='2023-1-1', major='计算机', paper=Paper.objects.get(id=1))
        temp_class = Clazz.objects.filter(id=1)
        temp.clazzs.set(temp_class) 

    def test_name_label(self):
        exam=Exam.objects.get(id=1)
        field_label = exam._meta.get_field('name').verbose_name
        self.assertEquals(field_label,"考试名称")

    def test_exam_date_label(self):
        exam=Exam.objects.get(id=1)
        field_label = exam._meta.get_field('exam_date').verbose_name
        self.assertEquals(field_label,"考试日期")

    def test_total_time_label(self):
        exam=Exam.objects.get(id=1)
        field_label = exam._meta.get_field('total_time').verbose_name
        self.assertEquals(field_label,"时长")

    def test_paper_label(self):
        exam=Exam.objects.get(id=1)
        field_label = exam._meta.get_field('paper').verbose_name
        self.assertEquals(field_label,"试卷")

    def test_major_label(self):
        exam=Exam.objects.get(id=1)
        field_label = exam._meta.get_field('major').verbose_name
        self.assertEquals(field_label,"专业")

    def test_tips_label(self):
        exam=Exam.objects.get(id=1)
        field_label = exam._meta.get_field('tips').verbose_name
        self.assertEquals(field_label,"考生须知")

    def test_clazzs_label(self):
        exam=Exam.objects.get(id=1)
        field_label = exam._meta.get_field('clazzs').verbose_name
        self.assertEquals(field_label,"参加考试的班级")

    def test_major_max_length(self):
        exam=Exam.objects.get(id=1)
        max_length = exam._meta.get_field('major').max_length
        self.assertEquals(max_length,20)

    def test_name_max_length(self):
        exam=Exam.objects.get(id=1)
        max_length = exam._meta.get_field('name').max_length
        self.assertEquals(max_length,20)

    def test_object_name(self):
        exam=Exam.objects.get(id=1)
        expected_object_name = '%s' % (exam.name)
        self.assertEquals(expected_object_name,str(exam))



class SubjectiveAnswerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Subjective.objects.create(question='问题1', answer_template='1234567答题的模板', level='2')
        number_of_users = 13
        for user_num in range(number_of_users):
            User.objects.create(username='user%s' % user_num, password = '654321%s' % user_num,)
        Clazz.objects.create(year='2020', major='计算机', clazz='1')
        Student.objects.create(name='syq', user=User.objects.get(id=1), gender='f', clazz=Clazz.objects.get(id=1))
        Paper.objects.create(name='试卷1', score=120)
        temp = Exam.objects.create(name='测试1', exam_date='2023-1-1', major='计算机', paper=Paper.objects.get(id=1))
        temp_class = Clazz.objects.filter(id=1)
        temp.clazzs.set(temp_class) 
        SubjectiveAnswer.objects.create(student=Student.objects.get(id=1), exam=Exam.objects.get(id=1), question=Subjective.objects.get(id=1), score=1, create_time="2023-1-1 1:00", update_time="2023-1-1 1:00")

    def test_student_label(self):
        answer=SubjectiveAnswer.objects.get(id=1)
        field_label = answer._meta.get_field('student').verbose_name
        self.assertEquals(field_label,"学生")

    def test_exam_label(self):
        answer=SubjectiveAnswer.objects.get(id=1)
        field_label = answer._meta.get_field('exam').verbose_name
        self.assertEquals(field_label,"考试")

    def test_question_label(self):
        answer=SubjectiveAnswer.objects.get(id=1)
        field_label = answer._meta.get_field('question').verbose_name
        self.assertEquals(field_label,"题目")

    def test_score_label(self):
        answer=SubjectiveAnswer.objects.get(id=1)
        field_label = answer._meta.get_field('score').verbose_name
        self.assertEquals(field_label,"分数")

    def test_answer_label(self):
        answer=SubjectiveAnswer.objects.get(id=1)
        field_label = answer._meta.get_field('answer').verbose_name
        self.assertEquals(field_label,"答案")

    def test_create_time_label(self):
        answer=SubjectiveAnswer.objects.get(id=1)
        field_label = answer._meta.get_field('create_time').verbose_name
        self.assertEquals(field_label,"创建日期")

    def test_update_time_label(self):
        answer=SubjectiveAnswer.objects.get(id=1)
        field_label = answer._meta.get_field('update_time').verbose_name
        self.assertEquals(field_label,"修改日期")

    def test_identifier_label(self):
        answer=SubjectiveAnswer.objects.get(id=1)
        field_label = answer._meta.get_field('identifier').verbose_name
        self.assertEquals(field_label,"标识符")

    def test_identifier_max_length(self):
        answer=SubjectiveAnswer.objects.get(id=1)
        max_length = answer._meta.get_field('identifier').max_length
        self.assertEquals(max_length,8)

    def test_object_name(self):
        answer=SubjectiveAnswer.objects.get(id=1)
        expected_object_name = f'{answer.student}的{answer.question}为{answer.score}分'
        self.assertEquals(expected_object_name,str(answer))
