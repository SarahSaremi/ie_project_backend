from django.urls import path

from cands.views.suggestion import SuggestionRecordView, StudentSuggestions, UpdateSuggestionStateViewSet
from cands.views.user import StudentRecordView

app_name = 'cands'
urlpatterns = [
    path('student/', StudentRecordView.as_view()),
    path('suggestion/', SuggestionRecordView.as_view()),
    path('student_suggestions/', StudentSuggestions.as_view({'get': 'list'})),
    path('update_suggestion_state/<int:pk>/', UpdateSuggestionStateViewSet.as_view({'post': 'update'})),
]