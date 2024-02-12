from django.contrib import admin
from .models import Teacher, Parent, Student


class HideLastLoginMixin:
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:
            form.base_fields.pop('last_login', None)
        return form


@admin.register(Teacher)
class TeacherAdmin(HideLastLoginMixin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_editable = ('email',)
    list_display_links = ('first_name', 'last_name')


@admin.register(Parent)
class ParentAdmin(HideLastLoginMixin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_editable = ('email',)
    list_display_links = ('first_name', 'last_name')


@admin.register(Student)
class StudentAdmin(HideLastLoginMixin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth')
    list_editable = ('email', 'date_of_birth')
    list_filter = ('first_name', 'last_name')
    list_display_links = ('first_name', 'last_name')
