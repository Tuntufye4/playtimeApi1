from rest_framework import viewsets
from .models import  GameDetails 
from .serializers import GamesDetailsSerializer
     
    
class GamesDetailsViewSet(viewsets.ModelViewSet):
    queryset = GameDetails.objects.all()
    serializer_class = GamesDetailsSerializer                                             