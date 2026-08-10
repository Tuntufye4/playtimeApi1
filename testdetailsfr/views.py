from rest_framework import viewsets
from .models import  TestsDetailsFr 
from .serializers import TestsDetailsFrSerializer
     
    
class TestsDetailsFrViewSet(viewsets.ModelViewSet):
    queryset = TestsDetailsFr.objects.all()
    serializer_class = TestsDetailsFrSerializer                                                           