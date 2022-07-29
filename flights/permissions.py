import datetime

from rest_framework.permissions import BasePermission

class HasAuthority(BasePermission):
    message = "You're not authorized to view this"

    def  has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.is_staff


class IsMoreThan3Days(BasePermission):
    message = "Too Early too changed."

    def has_object_permission(self, request, view, obj):
        return datetime.date.today() - 3 > obj.date