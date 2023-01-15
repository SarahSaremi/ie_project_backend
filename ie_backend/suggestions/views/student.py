from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response

from suggestions.models import Student
from suggestions.serializers.student import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



