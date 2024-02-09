from django.contrib import admin
from .models import Person, Teacher, Parent, Student


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_editable = ('email',)
    list_display_links = ('first_name', 'last_name')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_editable = ('email',)
    list_display_links = ('first_name', 'last_name')


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_editable = ('email',)
    list_display_links = ('first_name', 'last_name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth')
    list_editable = ('email', 'date_of_birth')
    list_display_links = ('first_name', 'last_name')
