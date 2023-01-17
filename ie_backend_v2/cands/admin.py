from django.contrib import admin

from cands.models.user import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_number', 'name']


admin.site.register(Student, StudentAdmin)
