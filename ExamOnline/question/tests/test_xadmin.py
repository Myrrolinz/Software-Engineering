from django.test import TestCase
#from index.models import User

import xadmin

from user.models import Student, Teacher, Clazz
from import_export import resources

from user.resource import StudentResource
from user.adminx import ClazzAdmin, StudentAdmin, TeacherAdmin

# Create your tests here.
class ClazzAdminTest(TestCase):
    """班级模型测试"""

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Clazz.objects.create(year='2020', major='计算机', clazz='1')

    def test_admin(self):
        admin = ClazzAdmin()
        self.assertEquals(admin.list_display, ['id', 'year', 'major', 'clazz'])
        self.assertEquals(admin.list_filter, ['year', 'major'])
        self.assertEquals(admin.search_fields, ['id', 'year', 'major', 'clazz'])
        self.assertEquals(admin.list_display_links, ['clazz'])
        self.assertEquals(admin.list_per_page, 10)
        self.assertEquals(admin.model_icon, 'fa fa-institution ')



class StudentAdminTest(TestCase):
    """班级模型测试"""

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Clazz.objects.create(year='2020', major='计算机', clazz='1')

    def test_admin(self):
        admin = StudentAdmin()
        self.assertEquals(admin.list_display, ['id', 'name', 'user', 'gender', 'clazz'])
        self.assertEquals(admin.list_filter, ['gender', 'clazz'])
        self.assertEquals(admin.search_fields, ['id', 'name', 'clazz'])
        self.assertEquals(admin.list_display_links, ['name'])
        self.assertEquals(admin.list_per_page, 10)
        self.assertEquals(admin.model_icon, 'fa fa-user-circle-o')
        self.assertEquals(admin.relfield_style, 'fk-ajax')
        self.assertEquals(admin.import_export_args, {'import_resource_class' : StudentResource})



class TeacherAdminTest(TestCase):
    """班级模型测试"""

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Clazz.objects.create(year='2020', major='计算机', clazz='1')
        
    def test_admin(self):
        admin = TeacherAdmin()
        self.assertEquals(admin.list_display, ['id', 'name', 'user', 'gender', 'title', 'institute'])
        self.assertEquals(admin.list_filter, ['gender', 'title', 'institute'])
        self.assertEquals(admin.search_fields, ['id', 'name'])
        self.assertEquals(admin.list_display_links, ['name'])
        self.assertEquals(admin.list_per_page, 10)
        self.assertEquals(admin.model_icon, 'fa fa-graduation-cap')

    