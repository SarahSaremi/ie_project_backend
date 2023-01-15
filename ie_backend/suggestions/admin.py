from django.contrib import admin

from suggestions.models import Student, User, Suggestion


class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_number', 'name']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'name']


class SuggestionAdmin(admin.ModelAdmin):
    list_display = ['subject', 'related_department', 'state']


admin.site.register(Student, StudentAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Suggestion, SuggestionAdmin)
