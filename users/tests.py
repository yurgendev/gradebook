from django.test import TestCase
from .models import Teacher, Parent, Student


class UsersModelsTest(TestCase):
    def test_teacher_str(self):
        teacher = Teacher.objects.create(
            first_name='Oksana',
            last_name='Yanchenko',
            middle_name='Yuriievna',
            email='op@ukraine.com'
        )

        self.assertEqual(
            str(teacher),
            'Yanchenko Oksana Yuriievna'
        )

    def test_parent_str(self):
        parent = Parent.objects.create(
            first_name='Anatolii',
            last_name='Ivanov',
            middle_name='',
            email='anatol@example.com'
        )
        self.assertEqual(str(parent), 'Ivanov Anatolii')

    def test_student_str(self):
        student = Student.objects.create(
            first_name='Vlad',
            last_name='Saloevskii',
            email='vlad@example.com'
        )
        self.assertEqual(str(student), 'Saloevskii Vlad')
