from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from suggestions.models import Student
from suggestions.serializers.student import StudentSerializer, RegisterStudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RegisterStudentAPI(generics.CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = RegisterStudentSerializer


class StudentDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self,request,*args,**kwargs):
        student = Student.objects.get(id=request.user.id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
