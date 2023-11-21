from rest_framework import views, response, permissions, status
from member.models import Member
from member.serializers import MemberSerializer


# Create your views here.
class MemberAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = Member.objects.all()
        serializer_class = MemberSerializer(queryset, many=True)

        return response.Response(data=serializer_class.data, status=status.HTTP_200_OK)
