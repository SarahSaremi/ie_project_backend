from rest_framework import serializers

from cands.models.suggestion import Suggestion
from cands.models.user import Student


class SuggestionSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.name')

    class Meta:
        model = Suggestion
        fields = '__all__'

    def create(self, validated_data):
        validated_data['student'] = Student.objects.get(id=validated_data['student'])
        suggestion = Suggestion.objects.create(**validated_data)
        return suggestion
