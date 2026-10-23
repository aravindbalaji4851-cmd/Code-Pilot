from rest_framework.permissions import BasePermission

from accounts.models import User

class IsAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.created_by