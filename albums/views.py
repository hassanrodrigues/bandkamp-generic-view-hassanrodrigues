from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Album
from .serializers import AlbumSerializer
from drf_spectacular.utils import extend_schema


class AlbumView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @extend_schema(
        tags=["Albums"],
        summary="Listar albums",
        description="EndPoint para listar todos os albums do usuário",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        tags=["Albums"],
        summary="Criar album",
        description="EndPoint para criar um album",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
