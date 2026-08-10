from django.db import models
from django.conf import settings          
        
class LearningDetails(models.Model):
    input = models.CharField(max_length=100, null=True) 
    title = models.CharField(max_length=100, null=True)     
    session_date = models.DateTimeField(null=True) 
    con_audio = models.URLField(max_length=250, null=True)
                         
              
    def __str__(self):   
        return f"{self.input}"       
                                 