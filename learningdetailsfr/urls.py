from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LearningDetailsFrViewSet

router = DefaultRouter()
router.register(r'', LearningDetailsFrViewSet, basename='learningdetailsfr')             

urlpatterns = router.urls                                    