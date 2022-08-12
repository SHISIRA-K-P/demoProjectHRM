from re import M
from django.db import models
from userApi.models import User

# Create your models here.

class Leave(models.Model):
    
    date_from=models.DateField(auto_now=True,null=True)
    date_to=models.DateField(auto_now=True,null=True)
    leave_status= (
        ('select', 'select'),
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('cancel', 'cancel'),
         ('reject', 'reject'),
    )
      
    status=models.CharField(choices=leave_status,default="select",max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True) 

    def __str__(self):
        return self.status
    


