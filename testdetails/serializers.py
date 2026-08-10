from rest_framework import serializers
from .models import TestsDetails  

class TestsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestsDetails
        fields = '__all__'                            