from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from suggestions.models.user import Student


class StudentSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = Student.objects.create_user(**validated_data)
        return user

    class Meta:
        model = Student
        fields = (
            'username',
            'name',
            'phone_number',
            'password',
            'student_number',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Student.objects.all(),
                fields=['username', 'phone_number']
            )
        ]