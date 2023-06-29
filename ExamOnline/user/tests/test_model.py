from django.test import TestCase
#from index.models import User
from user.models import Clazz

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