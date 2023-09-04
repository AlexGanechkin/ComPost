from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj) -> bool:
        return obj.author.username == request.user.username or request.user.is_staff


class CommentatorPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj) -> bool:
        return obj.commentator.username == request.user.username or request.user.is_staff
