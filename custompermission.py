#custom permission that checks who is creating the user
from rest_framework import permissions
from app.models import CustomUser

class CustomPermission(permissions.BasePermission):
    """checks whose creating the user"""
    def has_permission(self, request, view):
        try:
            #disallows creation of a superuser by anyone
            if 'is_superuser' in request.data:
                return false
            
            #ensures the user_type field is in the data provided
            if 'user_type' not in request.data:
                return True

            if request.data['user_type'] == 'A':
                #user type A can only be created by users of type B C and D
                return request.user and request.user.is_authenticated and request.user.user_type in ('B', 'C')
            elif request.data['user_type'] == 'B':
                #user type B can only be created by user of type C
                return request.user and request.user.is_authenticated and request.user.user_type == 'C'
            elif request.data['user_type'] == 'C':
                #user type C can only be created by superuser
                return request.user and request.user.is_authenticated and request.user.is_superuser
            else:
                #all other user types can be created by anyone
                return True
        except:
            return False
