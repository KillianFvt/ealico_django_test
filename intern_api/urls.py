from django.urls import path, include, re_path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(r"element", views.ElementViewSet, basename='element')


urlpatterns = [
    path('', include(router.urls)),
    re_path(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]
