"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import permissions, routers
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from ping import views as ping_views
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
import ssapi.views as ssapi_views

schema_view = get_schema_view(
    openapi.Info(
        title="SSAPI",
        default_version="v1",
    ),
    public=False,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r"users", ssapi_views.UserViewSet)

urlpatterns = [
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(
        r"^$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    url(r"^ping/", ping_views.Ping.as_view(), name="ping"),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^", include(router.urls)),
    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
