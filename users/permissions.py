from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверяет, является ли пользователь владельцем"""
    message = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
