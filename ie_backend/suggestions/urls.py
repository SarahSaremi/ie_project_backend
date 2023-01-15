from django.urls import path
from .views.student import StudentViewSet

urlpatterns = [
    path('students/', StudentViewSet.as_view({
        'get': 'list'
    }), name='students'),
]
