from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from user.views import CustomBackend, jwt_response_payload_handler, RegisterViewSet, UpdatePwdApi, StudentViewSet, ClazzListViewSet
from django.db.models import Q

from django.contrib.auth.hashers import make_password, check_password 
from user.models import Student, Clazz
from user.serializers import StudentSerializer, UserDetailSerializer, ClazzSerializer

# Create your tests here.


class CustomBackendTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_users = 13
        for user_num in range(number_of_users):
            User.objects.create(username='user%s' % user_num, password = '654321%s' % user_num,)
        Clazz.objects.create(year='2020', major='计算机', clazz='1')
        Student.objects.create(name='syq', user=User.objects.get(id=1), gender='f', clazz=Clazz.objects.get(id=1))
    
    def test_authenticate(self):
        backend=CustomBackend()
        user1 = backend.authenticate(username='user0', password = '6543210')
        #user1 = User.objects.get(Q(username='user0') | Q(mobile='user0'))
        #if check_password('6543210', make_password('6543210')):
        #    self.assertEqual(0, 1)
        self.assertEqual(user1, User.objects.get(id=1))

    def test_jwt_response_payload_handler(self):

        token = '1'
        user = User.objects.get(id=1)
        result = jwt_response_payload_handler(token=token, user=user)
        expect = {
            'token': token,
            'user': UserDetailSerializer(user, context={'request': None}).data,
            'student': StudentSerializer(Student.objects.get(id=1), context={'request': None}).data
        }

        self.assertEqual(result, expect)

    '''
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'templates/login.html')
    '''
