from rest_framework.permissions import BasePermission


class IsCurrentUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.email, request.user.email)
        return obj.email == request.user.email
