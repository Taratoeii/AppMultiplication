from django.db import models

class Numbercal(models.Model):
    Number_text = models.CharField(max_length=1)
    
    def __str__(self):
        return self.Number_text