from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase

# get the custom user model
User = get_user_model()


class UserTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='testpw', user_type=User.STUDENT)
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='testpw')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='testpw')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_user_type(self):
        user = User.objects.get(username='test')
        self.assertFalse(user.user_type is not User.STUDENT)
