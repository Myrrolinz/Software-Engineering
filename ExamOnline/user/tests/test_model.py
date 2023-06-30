from django.test import TestCase
#from index.models import User
from user.models import Clazz, Student, Teacher
from django.contrib.auth.models import User

# Create your tests here.
# Clazz中的模型设置均按照默认的升序排列，因此不进行测试
class ClazzModelTest(TestCase):
    """班级模型测试"""

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Clazz.objects.create(year='2020', major='计算机', clazz='1')

    def test_year_label(self):
        clazz_temp=Clazz.objects.get(id=1)
        field_label = clazz_temp._meta.get_field('year').verbose_name
        self.assertEquals(field_label,"年级")

    def test_major_label(self):
        clazz_temp=Clazz.objects.get(id=1)
        field_label = clazz_temp._meta.get_field('major').verbose_name
        self.assertEquals(field_label,"专业")

    def test_clazz_label(self):
        clazz_temp=Clazz.objects.get(id=1)
        field_label = clazz_temp._meta.get_field('clazz').verbose_name
        self.assertEquals(field_label,"班级")

    def test_year_max_length(self):
        clazz_temp=Clazz.objects.get(id=1)
        max_length = clazz_temp._meta.get_field('year').max_length
        self.assertEquals(max_length,20)

    def test_major_max_length(self):
        clazz_temp=Clazz.objects.get(id=1)
        max_length = clazz_temp._meta.get_field('major').max_length
        self.assertEquals(max_length,20)

    def test_clazz_max_length(self):
        clazz_temp=Clazz.objects.get(id=1)
        max_length = clazz_temp._meta.get_field('clazz').max_length
        self.assertEquals(max_length,20)

    def test_object_name(self):
        clazz_temp=Clazz.objects.get(id=1)
        expected_object_name = '%s%s%s' % (clazz_temp.year, clazz_temp.major, clazz_temp.clazz)
        self.assertEquals(expected_object_name,str(clazz_temp))


# Student中的模型设置均按照默认的升序排列，因此不进行测试
class StudentModelTest(TestCase):
    """班级模型测试"""

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Clazz.objects.create(year='2020', major='计算机', clazz='1')
        User.objects.create(username='user0', password = '6543210')
        Student.objects.create(name='张三', user=User.objects.get(id=1), gender='m', clazz=Clazz.objects.get(id=1))

    def test_name_label(self):
        student=Student.objects.get(id=1)
        field_label = student._meta.get_field('name').verbose_name
        self.assertEquals(field_label, "姓名")
    
    def test_user_label(self):
        student=Student.objects.get(id=1)
        field_label = student._meta.get_field('user').verbose_name
        self.assertEquals(field_label, "用户")

    def test_gender_label(self):
        student=Student.objects.get(id=1)
        field_label = student._meta.get_field('gender').verbose_name
        self.assertEquals(field_label, "性别")

    def test_clazz_label(self):
        student=Student.objects.get(id=1)
        field_label = student._meta.get_field('clazz').verbose_name
        self.assertEquals(field_label, "班级")

    def test_name_max_length(self):
        student=Student.objects.get(id=1)
        max_length = student._meta.get_field('name').max_length
        self.assertEquals(max_length,20)

    def test_gender_max_length(self):
        student=Student.objects.get(id=1)
        max_length = student._meta.get_field('gender').max_length
        self.assertEquals(max_length,1)

    def test_object_name(self):
        student=Student.objects.get(id=1)
        expected_object_name = '%s' % (student.name)
        self.assertEquals(expected_object_name,str(student))


# Teacher中的模型设置均按照默认的升序排列，因此不进行测试
class TeacherModelTest(TestCase):
    """班级模型测试"""

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        User.objects.create(username='user0', password = '6543210')
        Teacher.objects.create(name='张三', user=User.objects.get(id=1), gender='女', title='教授', institute='计算机学院')

    def test_name_label(self):
        teacher=Teacher.objects.get(id=1)
        field_label = teacher._meta.get_field('name').verbose_name
        self.assertEquals(field_label, "姓名")
    
    def test_user_label(self):
        teacher=Teacher.objects.get(id=1)
        field_label = teacher._meta.get_field('user').verbose_name
        self.assertEquals(field_label, "用户")

    def test_gender_label(self):
        teacher=Teacher.objects.get(id=1)
        field_label = teacher._meta.get_field('gender').verbose_name
        self.assertEquals(field_label, "性别")

    def test_title_label(self):
        teacher=Teacher.objects.get(id=1)
        field_label = teacher._meta.get_field('title').verbose_name
        self.assertEquals(field_label, "职称")

    def test_institute_label(self):
        teacher=Teacher.objects.get(id=1)
        field_label = teacher._meta.get_field('institute').verbose_name
        self.assertEquals(field_label, "学院")

    def test_name_max_length(self):
        teacher=Teacher.objects.get(id=1)
        max_length = teacher._meta.get_field('name').max_length
        self.assertEquals(max_length,20)

    def test_gender_max_length(self):
        teacher=Teacher.objects.get(id=1)
        max_length = teacher._meta.get_field('gender').max_length
        self.assertEquals(max_length,1)

    def test_title_max_length(self):
        teacher=Teacher.objects.get(id=1)
        max_length = teacher._meta.get_field('title').max_length
        self.assertEquals(max_length,5)

    def test_institute_max_length(self):
        teacher=Teacher.objects.get(id=1)
        max_length = teacher._meta.get_field('institute').max_length
        self.assertEquals(max_length,20)

    def test_object_name(self):
        teacher=Teacher.objects.get(id=1)
        expected_object_name = '%s' % (teacher.name)
        self.assertEquals(expected_object_name,str(teacher))