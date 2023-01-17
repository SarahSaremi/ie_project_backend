from rest_framework import serializers

from cands.models.suggestion import Suggestion
from cands.models.user import Student


class SuggestionSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.name')
    student_number = serializers.CharField(source='student.student_number')

    class Meta:
        model = Suggestion
        fields = '__all__'

    def create(self, validated_data):
        validated_data['student'] = Student.objects.get(id=validated_data['student'])
        suggestion = Suggestion.objects.create(**validated_data)
        return suggestion

    def update(self, instance, validated_data):
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance
