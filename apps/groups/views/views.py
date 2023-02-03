from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, DjangoObjectPermissions
from rest_framework.viewsets import ModelViewSet

from groups.models import Branch, Room, Course
from groups.serializers import BranchModelSerializer, \
    RoomListModelSerializer, RoomCreateModelSerializer, HomeModelSerializer
from shared.permissions import IsAdministrator


class BranchModelViewSet(ModelViewSet):
    serializer_class = BranchModelSerializer
    queryset = Branch.objects.all()
    parser_classes = (MultiPartParser,)
    permission_classes = IsAuthenticated, DjangoObjectPermissions, IsAdministrator


class RoomModelViewSet(ModelViewSet):
    serializer_class = RoomCreateModelSerializer
    queryset = Room.objects.all()
    permission_classes = IsAuthenticated, DjangoObjectPermissions, IsAdministrator

    def get_serializer_class(self):
        if self.action == 'list':
            return RoomListModelSerializer
        return super().get_serializer_class()


class HomeListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = HomeModelSerializer
    permission_classes = IsAuthenticated, DjangoObjectPermissions, IsAdministrator
