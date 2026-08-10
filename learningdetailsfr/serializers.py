from rest_framework import serializers

from .models import LearningDetailsFr


class LearningDetailsFrSerializer(serializers.ModelSerializer):

    class Meta:
        model = LearningDetailsFr    
   
        fields = [
            "id",          
            "input",         
            "session_date",
        
        ]      

        read_only_fields = [
            "id",
            "session_date",      
        ]    