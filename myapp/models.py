from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth

class Todo(models.Model):
    task=models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateField()
    is_complete=models.BooleanField(default=False)
    
    def __str__(self):
        return self.task+" at "+str(self.created_at)
    

class profile(models.Model):
    demo_title=models.CharField(max_length=40)
    profile_pic=models.ImageField(upload_to='profile_pic/')
    
    