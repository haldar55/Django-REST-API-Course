from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit only their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: # doesn't make any changes to the object
            return True
        
        return obj.id == request.user.id
    

class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to edit/update only their own status"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit/update their own status"""
        if request.method in permissions.SAFE_METHODS: # doesn't make any changes to the object
            return True
        
        return obj.user_profile.id == request.user.id
