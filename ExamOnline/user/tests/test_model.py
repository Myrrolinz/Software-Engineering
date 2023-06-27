from django.test import TestCase
from index.models import User

# Create your tests here.
class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        User.objects.create(username='root', password='123456')

    def test_username_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'用户号')

    def test_password_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEquals(field_label,'密码')

    def test_username_max_length(self):
        user=User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length,15)

    def test_password_max_length(self):
        user=User.objects.get(id=1)
        max_length = user._meta.get_field('password').max_length
        self.assertEquals(max_length,150)