from django.db import models

class Number(models.Model):
    Number_text = models.CharField(max_length=1)
    count = models.IntegerField(default=1)
    
    def __str__(self):
        return self.Number_text