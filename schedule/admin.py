from django.contrib import admin
from .models import SchoolClass, Lesson, Comment, Grade, CalendarEvent



class SchoolClassAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('students').order_by('students__last_name', 'students__first_name')


admin.site.register(SchoolClass, SchoolClassAdmin)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(Grade)
admin.site.register(CalendarEvent)
