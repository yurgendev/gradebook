from django.db import models
from datetime import datetime, timedelta


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        components = [self.last_name, self.first_name, self.middle_name]
        formatted_str = ' '.join(component for component in components if component)
        return formatted_str.strip()


class Teacher(Person):
    pass


class Parent(Person):
    email = models.EmailField(unique=False)


class Student(Person):
    date_of_birth = models.DateField(null=True, blank=True)
    middle_name = None

    @classmethod
    def get_upcoming_birthdays(cls):
        today = datetime.today().date()
        thirty_days_later = today + timedelta(days=30)
        return cls.objects.filter(date_of_birth__month__gte=today.month, date_of_birth__day__gte=today.day,
                                  date_of_birth__month__lte=thirty_days_later.month,
                                  date_of_birth__day__lte=thirty_days_later.day)
