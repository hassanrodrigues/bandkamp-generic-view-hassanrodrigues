from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from .serializers import UserSerializer
from .permissions import IsAccountOwner
from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=["Users"],
    summary="Criar usuário",
    description="Rota para criar usuários",
)
class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        tags=["Users"],
        summary="Listar um usuário",
        description="EndPoint para listar apenas um usuário",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=["Users"],
        summary="Editar um usuário",
        description="EndPoint para editar apenas um usuário",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        tags=["Users"],
        summary="Editar parcialmente um usuário",
        description="EndPoint para editar parcialmente apenas um usuário",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=["Users"],
        summary="Deletar um usuário",
        description="EndPoint para deletar apenas um usuário",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
