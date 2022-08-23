"""
Views for the user API
"""

from django.shortcuts import render  # noqa

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    # Super class - CreateAPIView
    # -> post 구현 (나머지 x)

    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    # Super class - RetrieveUpdateAPIView
    # -> get, put, patch 구현 (post 구현 x)

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # Override
    #   get 요청시 header 의 token 값으로 user를 찾아 Response 한다
    def get_object(self):
        """Retrieve and return the authenticated user"""
        return self.request.user


class CreateTokenView(ObtainAuthToken):
    """
    Create a new auth token for user

    * Override serializer_class
        to customized class (user.serializers.AuthTokenSerializer)
        instead of default AuthTokenSerializer
            cause of default base user model consist of username and password
            But this project uses user model as email and password
    """

    serializer_class = AuthTokenSerializer

    # For availability in browser
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
