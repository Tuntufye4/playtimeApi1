from rest_framework import viewsets
from .models import  TestsDetails 
from .serializers import TestsDetailsSerializer
     
    
class TestsDetailsViewSet(viewsets.ModelViewSet):
    queryset = TestsDetails.objects.all()
    serializer_class = TestsDetailsSerializer                                             