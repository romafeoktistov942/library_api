from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from library.pagination import CustomPagination
from users.models import User
from users.permissions import IsModer, IsSelf, IsSuperUser
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления пользователями.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get_permissions(self):
        """
        Переопределение метода для назначения прав доступа.
        """
        if self.action == "list":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "create":
            self.permission_classes = [~IsModer]
        elif self.action in ["update", "retrieve", "partial_update"]:
            self.permission_classes = [IsAuthenticated, IsSuperUser | IsSelf]
        elif self.action == "destroy":
            self.permission_classes = [IsAuthenticated, ~IsModer | IsSelf]
        return super().get_permissions()

    def perform_create(self, serializer):
        """
        Переопределение метода для хэширования пароля перед сохранением
        пользователя и предотвращения создания суперпользователей или стафа.
        """
        if serializer.validated_data.get(
            "is_superuser"
        ) or serializer.validated_data.get("is_staff"):
            raise PermissionDenied(
                "Нельзя создать суперпользователя или стафа через API."
            )
        user = serializer.save()
        user.set_password(user.password)
        user.save()
