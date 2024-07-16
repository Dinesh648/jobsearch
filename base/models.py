from django.db import models

# Create your models here.
class Room(models.Model):
    #host #topic #participants
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    updated = models.DateTimeField(auto_now=True) # everytime the model is changed this will log the time
    created = models.DateTimeField(auto_now_add=True) # will save it for the first save
    
    def __str__(self) -> str:
        return str(self.name)