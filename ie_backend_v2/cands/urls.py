from django.urls import path

from cands.views.user import StudentRecordView

app_name = 'cands'
urlpatterns = [
    path('student/', StudentRecordView.as_view()),
]