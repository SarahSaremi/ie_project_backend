from django.contrib import admin

from suggestions.models import Student, User


class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_number', 'name']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'name']


admin.site.register(Student, StudentAdmin)
admin.site.register(User, UserAdmin)
