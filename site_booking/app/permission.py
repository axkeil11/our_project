from rest_framework import permissions


class IsHotelOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status =='owner' :
            return True
        return False


class IsClient(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status == 'client':
            return True
        return False