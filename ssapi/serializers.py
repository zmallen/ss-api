from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    token = serializers.CharField(source="auth_token.key", read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "token",
        )
        read_only_fields = ("id", "token", "groups")
