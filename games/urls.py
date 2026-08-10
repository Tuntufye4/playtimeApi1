from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GamesDetailsViewSet

router = DefaultRouter()
router.register(r'', GamesDetailsViewSet, basename='gamedetails')             

urlpatterns = router.urls                  