from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Lecturer, Module

"""
This contains some simple unit tests for the following models: Module, Lecturer
"""

# get the custom user model
User = get_user_model()


class ModuleTest(TestCase):

    def setUp(self):
        self.module_1 = Module.objects.create(title='module_test',
                                              content='content_test',
                                              credits=5)

        self.module_2 = Module.objects.create(title='module_test',
                                              content='content_test',
                                              credits=8)

    def tearDown(self):
        self.module_1.delete()
        self.module_2.delete()

    def test_str(self):
        self.assertEqual(str(self.module_1), self.module_1.title)

    def test_filter_modules_by_credits(self):
        """True if module_1 is in the result_set and module_2 is not"""
        result_set = Module.filter_modules_by_credits(5)
        self.assertTrue(self.module_1 in result_set and self.module_2 not in result_set)


class LecturerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='testpw', user_type=User.LECTURER)
        self.lecturer = Lecturer.objects.create(user=self.user, first_name='first_name_test',
                                                last_name='last_name_test')

    def tearDown(self):
        self.user.delete()
        self.lecturer.delete()

    def test_str(self):
        self.assertEqual(str(self.lecturer), f'{self.lecturer.first_name} {self.lecturer.last_name}')
