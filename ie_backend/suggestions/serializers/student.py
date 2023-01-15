from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from suggestions.models import Student, User


class StudentSerializer(serializers.ModelSerializer):
    suggestions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        return Student.objects.create_user(**validated_data)


class RegisterStudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    student_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Student.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = Student
        fields = ('username', 'password', 'name', 'student_number')

    def create(self, validated_data):
        student = Student.objects.create(
            name=validated_data['name'],
            username=validated_data['username'],
            password=validated_data['password'],
            phone_number=validated_data['phone_number'],
            student_number=validated_data['student_number']
        )
        student.save()
        return student