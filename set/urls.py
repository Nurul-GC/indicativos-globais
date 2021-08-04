import rest_framework.urls
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from indig.views import IndicativosViewSet

router = DefaultRouter()
router.register('indicativos', IndicativosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('master/', admin.site.urls),
    path('indig-auth/', include(rest_framework.urls, namespace='rest_framework'))
]
