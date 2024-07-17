from django.db import models

# Create your models here.
class Room(models.Model):
    #host #topic #participants
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    updated = models.DateTimeField(auto_now=True) # everytime the model is changed this will log the time
    created = models.DateTimeField(auto_now_add=True) # will save it for the first save
    
    def __str__(self) -> str:
        return self.name
    

class Message(models.Model):
    # user
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]