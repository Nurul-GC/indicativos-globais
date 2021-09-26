import rest_framework.urls
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from indig.views import IndicativosViewSet, index

router = DefaultRouter()
router.register('indicativos', IndicativosViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls, namespace='indicativos')),
    path('master/', admin.site.urls),
    path('indig-auth/', include(rest_framework.urls, namespace='rest_framework'))
]
