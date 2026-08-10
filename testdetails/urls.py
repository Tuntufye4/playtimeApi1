from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestsDetailsViewSet

router = DefaultRouter()
router.register(r'', TestsDetailsViewSet, basename='testdetails')             

urlpatterns = router.urls           