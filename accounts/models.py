from django.db import models
from main.models import BaseModel
import uuid

# Create your models here.
class UserProfile(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = models.CharField(max_length=128, blank=True, null=True)
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True,null=True)

    name = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=255,blank=True,null=True)
    country = models.ForeignKey('main.Country', on_delete=models.CASCADE,blank=True,null=True)
    is_verified = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
   

    class Meta:
        db_table = 'accounts__profile'
        verbose_name = 'user profile'
        verbose_name_plural = 'user profiles'
        ordering = ('name',)
        
    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.phone
        

class OtpRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=16)
    otp = models.PositiveIntegerField()
    email = models.EmailField(blank=True,null=True)
    attempts = models.PositiveIntegerField(default=1)
    is_applied = models.BooleanField(default=False)
    country = models.ForeignKey('main.Country', on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    date_updated = models.DateTimeField(db_index=True, auto_now_add=True)


    class Meta:
        db_table = 'accounts_otp_record'
        verbose_name = 'Otp Record'
        verbose_name_plural = 'Otp Records'
        ordering = ('-date_added',)
        
    def __str__(self):
        return self.phone