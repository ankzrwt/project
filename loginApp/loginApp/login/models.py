from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50,null=False)
    userName=models.CharField(max_length=50,null=False)
    
