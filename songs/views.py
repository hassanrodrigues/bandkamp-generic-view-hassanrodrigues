from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Song
from .serializers import SongSerializer


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
