"""
Views for the user API
"""

from django.shortcuts import render  # noqa

from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""

    """
    Override serializer_class
        to customized class (user.serializers.AuthTokenSerializer)  
        instead of default AuthTokenSerializer
            cause of default base user model consist of username and password
            But this project uses user model as email and password
    """
    serializer_class = AuthTokenSerializer

    # For availability in browser
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
