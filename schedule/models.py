from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from users.models import Teacher, Parent, Student # noqa


class Class(models.Model):
    class_name = models.CharField(max_length=50, unique=True, db_index=True)
    students = models.ManyToManyField(Student, related_name='classes')
    english_group = models.ManyToManyField(Student, related_name='english_groups')
    ukrainian_group = models.ManyToManyField(Student, related_name='ukrainian_groups')


class Lesson(models.Model):
    date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='lessons')
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subject} - {self.date} - {self.class_obj.class_name}"


GRADE_TYPES = (
    ('homework', 'Homework'),
    ('test', 'Test'),
    ('exam', 'Exam'),

)


class Grade(models.Model):
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    grade_type = models.CharField(max_length=50, choices=GRADE_TYPES)


class GradeComment(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    author = models.ForeignKey(Parent, on_delete=models.CASCADE)
    text = models.TextField()


class CalendarEvent(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    event_date = models.DateField()
    description = models.TextField()


class Comment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    author_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
