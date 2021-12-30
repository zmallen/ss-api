# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
import random
from django.shortcuts import render
from django.db import connections, OperationalError
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class Ping(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        """
        Health check, select 1 on current db connection
        """
        open_connections = connections.all()
        if not open_connections:
            logger.debug("Failed to get DB conn")
            return Response(status=500)
        conn = random.choice(open_connections)
        try:
            cursor = conn.cursor()
            cursor.execute("select 1")
            health_check = cursor.fetchone()[0]
            if health_check != 1:
                logger.debug("Health query failed")
                return Response(status=500)
        except OperationalError:
            logger.exception("Ping failure")
            return Response(status=500)
        return Response({}, status=200)
