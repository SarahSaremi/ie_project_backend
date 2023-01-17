from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from cands.models.suggestion import Suggestion
from cands.models.user import Student
from cands.serializers.suggestion import SuggestionSerializer


class SuggestionRecordView(APIView):
    def get(self, format=None):
        suggestion = Suggestion.objects.all()
        serializer = SuggestionSerializer(suggestion, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SuggestionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class StudentSuggestions(ViewSet):
    def list(self, request):
        student_id = request.GET.get('student_id', 2)
        queryset = Suggestion.objects.filter(student_id=student_id)
        serializer = SuggestionSerializer(queryset, many=True)
        return Response(serializer.data)


class UpdateSuggestionStateViewSet(ModelViewSet):
    queryset = Suggestion.objects.all()
    serializer_class = SuggestionSerializer

    def update(self, request, pk=None, *args, **kwargs):
        data = {"state": request.query_params['state'], }
        suggestion = Suggestion.objects.get(id=pk)
        serializer = self.serializer_class(instance=suggestion, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
