from django.contrib import admin
from .models import SchoolClass


class SchoolClassAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('students').order_by('students__last_name', 'students__first_name')


admin.site.register(SchoolClass, SchoolClassAdmin)
