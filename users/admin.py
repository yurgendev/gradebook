from django.contrib import admin

# Register your models here.


from .models import Person, Teacher, Parent, Student

admin.site.register(Person)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Student)
