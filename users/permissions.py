from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """Проверяем права на создание и удаление."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsOwner(permissions.BasePermission):
    """Проверяем права на просмотр и редактирование."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class IsSelf(permissions.BasePermission):
    """Проверяем права на просмотр и редактирование собственных данных."""

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsSuperUser(permissions.BasePermission):
    """Проверяем права суперпользователя."""

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
