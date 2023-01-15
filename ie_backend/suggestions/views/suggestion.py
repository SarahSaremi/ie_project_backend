from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from suggestions.models import Suggestion
from suggestions.serializers.suggestion import SuggestionSerializer


class SuggestionsViewSet(viewsets.ModelViewSet):
    queryset = Suggestion.objects.all()
    serializer_class = SuggestionSerializer


class SubmitSuggestionAPI(generics.CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = SuggestionSerializer


class StudentSuggestions(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def list(self, request):
        student_id = request.GET.get('student_id', 2)
        queryset = Suggestion.objects.filter(student_id=student_id)
        serializer = SuggestionSerializer(queryset, many=True)
        return Response(serializer.data)
