from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.created_by, '--', request.user)
        return obj.created_by == request.user
