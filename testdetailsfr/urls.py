from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestsDetailsFrViewSet

router = DefaultRouter()
router.register(r'', TestsDetailsFrViewSet, basename='testdetailsfr')             

urlpatterns = router.urls                        