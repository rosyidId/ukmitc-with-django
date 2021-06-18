# from app.models import Anggota
from rest_framework import viewsets, permissions
# from api.serializers import GroupSerializer, UserSerializer
# from django.contrib.auth.models import Group, User
from app.models import Anggota
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Anggota.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
