from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers.user import UserModelSerializer
from rest_framework.parsers import FormParser, MultiPartParser


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    parser_classes = (FormParser, MultiPartParser)

    queryset = User.objects.all()
    ordering = ['-date_joined']
    search_fields = ['username']
