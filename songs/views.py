from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Song
from .serializers import SongSerializer
from drf_spectacular.utils import extend_schema


class SongView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer

    def get_queryset(self):
        album_id = self.kwargs.get("pk")
        return Song.objects.filter(album_id=album_id)

    def perform_create(self, serializer):
        album_id = self.kwargs.get("pk")
        return serializer.save(album_id=album_id)

    @extend_schema(
        tags=["Songs"],
        summary="Listar músicas de determinado album",
        description="EndPoint para listar todas as músicas de determinado album",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        tags=["Songs"],
        summary="Criar música",
        description="EndPoint para criar uma música no album especificado",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
