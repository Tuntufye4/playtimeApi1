from django.db import models
from django.conf import settings          
        
class  GameDetails(models.Model):
    title = models.CharField(max_length=250, null=True) 
    total_questions = models.IntegerField(null=True)
    total_score = models.IntegerField(null=True)    
    session_date = models.DateField(null=True)                          
          
    def __str__(self):                                      
        return f"{self.title}"               
                                         