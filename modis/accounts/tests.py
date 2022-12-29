from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase

# Get the custom user model
User = get_user_model()


class UserTest(TestCase):
    """
    This tests simple authentication functionality for the custom user model.
    """

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_pw', user_type=User.STUDENT)
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct_user(self):
        # True if username, password and user_type are correct
        user = authenticate(username='test_user', password='test_pw')
        self.assertTrue((user is not None) and user.is_authenticated and user.user_type is User.STUDENT)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='test_pw')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test_user', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_user_type(self):
        user = User.objects.get(username='test_user')
        self.assertFalse(user.user_type is not User.STUDENT)
