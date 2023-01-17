from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from cands.models.user import Student


class StudentSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        student = Student.objects.create_user(**validated_data)
        return student

    class Meta:
        model = Student
        fields = (
            'username',
            'name',
            'phone_number',
            'student_number',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Student.objects.all(),
                fields=['username', 'student_number']
            )
        ]