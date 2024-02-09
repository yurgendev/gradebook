from django.contrib import admin
from .models import SchoolClass, Lesson, Comment, Grade, CalendarEvent


class SchoolClassAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('students').order_by('students__last_name', 'students__first_name')


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('class_name',)
    list_editable = ('class_name',)
    list_display_links = None


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_date', 'teacher', 'subject')
    list_editable = ('teacher', 'subject')
    list_display_links = ('lesson_date',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'author')
    list_editable = ('author',)
    list_display_links = ('text',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('value', 'student', 'lesson', 'grade_type')
    list_editable = ('student', 'lesson', 'grade_type')
    list_display_links = ('value',)


@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ('event_date', 'grade')
    list_editable = ('grade',)
    list_display_links = ('event_date',)
