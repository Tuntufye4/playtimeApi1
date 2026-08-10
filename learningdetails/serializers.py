from rest_framework import serializers

from .models import LearningDetails


class LearningDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = LearningDetails

        fields = [
            "id",
            "input",    
            "session_date",
        
        ]

        read_only_fields = [
            "id",
            "session_date",      
        ]