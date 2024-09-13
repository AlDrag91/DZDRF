from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """Проверка нахождения пользователя в группе модератора."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderators').exists()


class IsOwner(permissions.BasePermission):
    """Проверка пользователя своих курсов и уроков"""
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
