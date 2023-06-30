from django.test import TestCase
#from index.models import User

import xadmin

from import_export import resources

from user.models import Clazz
from exam.models import Exam, Grade, Paper,SubjectiveAnswer
from xadmin.views import CommAdminView, BaseAdminView
from xadmin.plugins.auth import UserAdmin
from exam.adminx import GlobalSetting, ExamAdmin

# Create your tests here.
class GlobalSettingTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Clazz.objects.create(year='2020', major='计算机', clazz='1')

    def test_admin(self):
        globalset = GlobalSetting()
        self.assertEquals(globalset.site_title, 'Python在线考试后台管理系统')
        self.assertEquals(globalset.site_footer, 'Design by Pengshengfu')


class ExamAdminTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Clazz.objects.create(year='2020', major='计算机', clazz='1')

    def test_admin(self):
        admin = ExamAdmin()
        self.assertEquals(admin.list_display, ['id', 'name', 'exam_date', 'total_time', 'paper', 'major', 'tips', 'clazzs'])
        self.assertEquals(admin.list_filter, ['major', 'exam_date'])
        self.assertEquals(admin.search_fields, ['id', 'name'])
        self.assertEquals(admin.list_display_links, ['name'])
        self.assertEquals(admin.list_per_page, 10)
        self.assertEquals(admin.model_icon, 'fa fa-book')
        self.assertEquals(admin.style_fields, {'clazzs': 'm2m_transfer'})
