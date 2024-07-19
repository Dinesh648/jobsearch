from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
import uuid
# Create your models here.

User = get_user_model()
#this extends the user class and contains additional information such as organisation name
class CustomUser(User):
    
    organisation = models.CharField(max_length=50, blank=True, null=True)
    work_email = models.EmailField(max_length=100, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.username

class Organisation(models.Model):
    
    organisation_Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    location = models.TextField(null=True, blank=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_organisation_name'),
        ]

    def __str__(self) -> str:
        return self.name
    
class JobOpenings(models.Model):
    
    role = models.CharField(max_length=50)
    job_Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organisation_Id = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='job_openings')
    description = models.TextField(max_length=100)
    
    def __str__(self) -> str:
        return self.role
    

class JobReferrals(models.Model):
    
    referral_Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_Id = models.ForeignKey(JobOpenings, on_delete=models.CASCADE, related_name='job_referrals')
    user_Id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='job_referrals')
    
    def __str__(self):
        return str(self.referral_Id)
    

class Room(models.Model):
    #host #topic #participants
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    updated = models.DateTimeField(auto_now=True) # everytime the model is changed this will log the time
    created = models.DateTimeField(auto_now_add=True) # will save it for the first save
    
    def __str__(self) -> str:
        return self.name
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]