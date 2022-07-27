import datetime

from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    message = "You must be the author of this article."

    def has_object_permission(self, request, view, obj):
        print("yujhmn")
        print("!!!!!!!!!!!!!",obj.date)

        if obj.date > datetime.date(obj.date.year, obj.date.month, obj.date.day + 3):
            return True
        else:
            return False
