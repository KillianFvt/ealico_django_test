from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('app/', include('app.urls')),
    path('admin/', admin.site.urls),
    path('api/', include("intern_api.urls")),
    path('api-auth/', include("rest_framework.urls")),
]
