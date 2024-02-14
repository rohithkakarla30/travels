from rest_framework.permissions import BasePermission, SAFE_METHODS

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_superuser)
    
class IsAuthenticated_obj(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and not request.user.is_superuser)
    
    def has_object_permissions(self,request,obj):
        
        return bool(obj.username==request.user and request.user.is_superuser==False)