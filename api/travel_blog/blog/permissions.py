from urllib import request
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

   """
   Пользовательское разрешение, позволяющее
   только владельцам объекта редактировать его
   """

   def has_object_permission(self, request, view, obj):
      if request.method in permissions.SAFE_METHODS:
        return True
      return obj.owner == request.user 