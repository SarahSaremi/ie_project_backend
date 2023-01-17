from django.urls import path
from .views.student import StudentViewSet, RegisterStudentAPI, StudentDetailAPI
from .views.suggestion import SuggestionsViewSet, StudentSuggestions
from .views.user import StudentRecordView

urlpatterns = [
    path('student_records/', StudentRecordView.as_view()),

    path('students/', StudentViewSet.as_view({'get': 'list'})),
    path('register/', RegisterStudentAPI.as_view()),
    path('get_student/', StudentDetailAPI.as_view()),

    path('all_suggestions/', SuggestionsViewSet.as_view({'get': 'list'})),
    path('get_suggestion/<int:pk>/', SuggestionsViewSet.as_view({
        'get': 'retrieve'
    })),
    path('student_suggestions/', StudentSuggestions.as_view({'get': 'list'})),
]
