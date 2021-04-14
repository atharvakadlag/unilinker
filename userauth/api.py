from rest_framework import viewsets, permissions
from .models import UnilinkerUser
from .serializers import UnilinkerUserSerializer


class UnilinkerUserViewset(viewsets.ModelViewSet):
    queryset = UnilinkerUser.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UnilinkerUserSerializer
