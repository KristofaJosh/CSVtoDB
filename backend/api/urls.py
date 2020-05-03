from django.urls import path, include
from rest_framework import routers
from .views import ZenoViewSet

router = routers.DefaultRouter()
router.register('all', ZenoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
