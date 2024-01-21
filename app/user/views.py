from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.parsers import MultiPartParser
from user.serializers import FileSerializer


class FileViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = FileSerializer
    parser_classes = [MultiPartParser]
