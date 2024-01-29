from django.test import TestCase
from schedule.models import SchoolClass, Lesson, Grade, CalendarEvent
from users.models import Teacher, Student

class SchoolClassModelTest(TestCase):
    def setUp(self):
        self.school_class = SchoolClass.objects.create(class_name='10A')

    def test_str(self):
        self.assertEqual(str(self.school_class), '10A')

class LessonModelTest(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')
        self.lesson = Lesson.objects.create(lesson_date='2022-01-01', teacher=self.teacher, subject='Math')

    def test_str(self):
        self.assertEqual(str(self.lesson), 'Math - 2022-01-01')

class GradeModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(first_name='Jane', last_name='Doe', email='jane.doe@example.com')
        self.teacher = Teacher.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')
        self.lesson = Lesson.objects.create(lesson_date='2022-01-01', teacher=self.teacher, subject='Math')
        self.grade = Grade.objects.create(value=5, student=self.student, lesson=self.lesson, grade_type='homework')

    def test_str(self):
        self.assertEqual(str(self.grade), '5')

class CalendarEventModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(first_name='Jane', last_name='Doe', email='jane.doe@example.com')
        self.teacher = Teacher.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')
        self.lesson = Lesson.objects.create(lesson_date='2022-01-01', teacher=self.teacher, subject='Math')
        self.grade = Grade.objects.create(value=5, student=self.student, lesson=self.lesson, grade_type='homework')
        self.calendar_event = CalendarEvent.objects.create(event_date='2022-01-01', grade=self.grade)
        self.calendar_event.lesson.add(self.lesson)
        self.calendar_event.student.add(self.student)

    def test_str(self):
        self.assertEqual(str(self.calendar_event), f"{self.lesson.subject} - {self.student.first_name} {self.student.last_name} - 2022-01-01")