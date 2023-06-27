from django.test import TestCase
from index.models import User
from django.urls import reverse

# Create your tests here.


class UserLoginViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_users = 13
        for user_num in range(number_of_users):
            User.objects.create(username='user%s' % user_num, password = '654321%s' % user_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'login.html')
