from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_student=models.BooleanField(default=False)
    name=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    address=models.TextField(null=True)
    image=models.ImageField(upload_to='profile')

class Complaints(models.Model):
    title=models.CharField(max_length=30)
    complaint=models.ForeignKey(Login,on_delete=models.CASCADE)
    reply=models.TextField(null=True)
    date=models.DateField(null=True)

class Notification(models.Model):
    subject=models.CharField(max_length=25)
    description=models.TextField(null=True)
    date=models.DateField(null=True)