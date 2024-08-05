from django.urls import path,include
from rest_framework.routers import DefaultRouter
from testapp.api.views import HydJobsCRUDCBV
router = DefaultRouter()
router.register('hydjobsinfo', HydJobsCRUDCBV)
urlpatterns = [
    path('', include(router.urls)),
]