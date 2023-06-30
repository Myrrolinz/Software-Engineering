from django.test import TestCase
#from index.models import User

import xadmin

from import_export import resources

from user.models import Clazz
from question.resource import ChoiceResource, FillResource, JudgeResource, SubjectiveResource
from question.adminx import ChoiceAdmin, FillAdmin, JudgeAdmin, SubjectiveAdmin

# Create your tests here.
class ChoiceAdminTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Clazz.objects.create(year='2020', major='计算机', clazz='1')

    def test_admin(self):
        admin = ChoiceAdmin()
        self.assertEquals(admin.list_display, ['id', 'question', 'answer_A', 'answer_B', 'answer_C', 'answer_D',
                    'right_answer', 'analysis', 'score', 'level'])
        self.assertEquals(admin.list_filter, ['level'])
        self.assertEquals(admin.search_fields, ['id', 'question'])
        self.assertEquals(admin.list_display_links, ['question'])
        self.assertEquals(admin.list_per_page, 10)
        self.assertEquals(admin.model_icon, 'fa fa-question-circle-o')
        self.assertEquals(admin.import_export_args, {'import_resource_class': ChoiceResource})



class FillAdminTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Clazz.objects.create(year='2020', major='计算机', clazz='1')

    def test_admin(self):
        admin = FillAdmin()
        self.assertEquals(admin.list_display, ['id', 'question', 'right_answer', 'analysis', 'score', 'level'])
        self.assertEquals(admin.list_filter, ['level'])
        self.assertEquals(admin.search_field, ['id', 'question'])
        self.assertEquals(admin.list_display_links, ['question'])
        self.assertEquals(admin.list_per_page, 10)
        self.assertEquals(admin.model_icon, 'fa fa-edit ')
        self.assertEquals(admin.import_export_args, {'import_resource_class': FillResource})



class SubjectiveAdminTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Clazz.objects.create(year='2020', major='计算机', clazz='1')

    def test_admin(self):
        admin = SubjectiveAdmin()
        self.assertEquals(admin.list_display, ['id', 'question', 'analysis', 'score', 'level'])
        self.assertEquals(admin.list_filter, ['level'])
        self.assertEquals(admin.search_field, ['id', 'question'])
        self.assertEquals(admin.list_display_links, ['question'])
        self.assertEquals(admin.list_per_page, 10)
        self.assertEquals(admin.model_icon, 'fa fa-laptop')
        self.assertEquals(admin.import_export_args, {'import_resource_class': SubjectiveResource})

    