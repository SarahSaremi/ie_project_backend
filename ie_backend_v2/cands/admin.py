from django.contrib import admin

from cands.models.suggestion import Suggestion
from cands.models.user import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_number', 'name']


class SuggestionAdmin(admin.ModelAdmin):
    list_display = ['subject', 'related_department', 'state']


admin.site.register(Student, StudentAdmin)
admin.site.register(Suggestion, SuggestionAdmin)
