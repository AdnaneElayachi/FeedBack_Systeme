"""
URL configuration for api_feedback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.views.generic import TemplateView

from api_feedback import settings
from api_feedback_apps.views import feedback_list, validate_all_feedbacks, validate_feedback
from django.urls import path, include
from api_feedback_apps.views import FeedbackModelViewSet
from rest_framework.routers import DefaultRouter

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Documentation interactive pour l'API Feedback",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r'feedback', FeedbackModelViewSet, basename='feedback')
urlpatterns = [


    path('', include(router.urls)),



     path('admin_tools/', include('admin_tools.urls')), 
    path("admin/", admin.site.urls),
    path("api/v1/", include("api_feedback_apps.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("validate_feedback/<int:feedback_id>/", validate_feedback, name="validate_feedback"),
    path("feedback_list/", feedback_list, name="feedback_list"),
        path('validate_all_feedbacks/', validate_all_feedbacks, name='validate_all_feedbacks'),


]



if settings.DEBUG:  # Vérifie si le mode DEBUG est activé
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)