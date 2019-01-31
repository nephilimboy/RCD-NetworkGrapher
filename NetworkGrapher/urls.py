from django.conf.urls import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('grapher.api_urls')),
    path('api/v1/', include('grapherEntities.api_urls')),
]
