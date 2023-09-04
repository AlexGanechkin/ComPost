from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj) -> bool:
        return obj.username == request.user.username or request.user.is_staff
