from rest_framework import serializers
from .models import TestsDetailsFr  

class TestsDetailsFrSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestsDetailsFr
        fields = '__all__'                                            