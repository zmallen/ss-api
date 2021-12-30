# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from ssapi.serializers import UserSerializer
from rest_framework import authentication, permissions
import logging

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
