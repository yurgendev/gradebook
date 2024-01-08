from django.db import models
from django.core.validators import EmailValidator



class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(validators=[EmailValidator(message="Invalid email")])

    def __str__(self):
        middle_initial = self.middle_name[0] if self.middle_name else ''
        return f"{self.last_name} {self.first_name[0]}{middle_initial}"


class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(validators=[EmailValidator(message="Invalid email")])

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(validators=[EmailValidator(message="Invalid email")])

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
