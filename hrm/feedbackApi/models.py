from django.db import models
from userApi.models import User

# Create your models here.

class Feedback(models.Model):
    
    content=models.CharField(max_length=250)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.content
    


