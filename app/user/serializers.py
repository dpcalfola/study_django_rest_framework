"""
Serializers for the user API view
"""

from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user"""

        # This method override ModelSerializer.update(instance, validated_data)
        #    Purpose:
        #        Password update should be optional

        # validated_data.pop('dictKey', None)
        # If validated_data has 'dictKey' data -> Retrieve value after that remove it
        # If validated_Data has not 'dictKey' data -> password = None
        password = validated_data.pop('password', None)

        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Custom serializer for user auth token"""

    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """
        Validate and authenticate the user
        -> It returns authenticated object
        """

        email = attrs.get('email')
        password = attrs.get('password')

        # authenticate():
        #    Django built in method
        #   -> Check user information is correct or not
        #   "If the given credentials are valid, return a User object"
        user = authenticate(
            # request=self... -> some kind of syntax
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
