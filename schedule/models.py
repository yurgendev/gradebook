from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django import forms
from users.models import Teacher, Parent, Student


class SchoolClass(models.Model):
    class_name = models.CharField(max_length=2, unique=True, db_index=True)
    students = models.ManyToManyField(Student, related_name='classes')

    class Meta:
        ordering = ['students__last_name', 'students__first_name']

    def __str__(self):
        return self.class_name


class Lesson(models.Model):
    SUBJECT_CHOICES = [
        ('math', 'Math'),
        ('it', 'IT'),
        ('english', 'English'),
        ('ukrainian', 'The Ukrainian Language'),
        ('deutch', 'Deutch'),
        ('geography', 'Geography'),
        ('art', 'Art'),
    ]

    lesson_date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)

    def __str__(self):
        return f"{self.get_subject_display()} - {self.lesson_date}"


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Parent, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.text} - {self.author}"


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
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.value


class CalendarEvent(models.Model):
    lesson = models.ManyToManyField(Lesson)
    student = models.ManyToManyField(Student)
    event_date = models.DateField()
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.lesson.subject} - {self.student.name} - {self.event_date}"


class CalendarEventForm(forms.ModelForm):
    event_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = CalendarEvent
        fields = ['lesson', 'student', 'event_date', 'grade']
