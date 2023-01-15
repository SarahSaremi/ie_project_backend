from rest_framework import serializers

from suggestions.models import Suggestion


class SuggestionSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.name')

    class Meta:
        model = Suggestion
        fields = '__all__'

    def create(self, validated_data):
        suggestion = Suggestion.objects.create(**validated_data)
        return suggestion
