from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(validators=[EmailValidator(message="Invalid email")])

    def __str__(self):
        middle_initial = self.middle_name[0] if self.middle_name else ''
        return f"{self.last_name} {self.first_name[0]}{middle_initial}"


class Student(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class Teacher(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class Parent(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
