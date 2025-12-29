from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Taskmodel(models.Model):
    PRIORITY_LEVEL= [('high', 'High'), ('medium', 'Medium'), ('low', 'Low')]
    STATUS_CURRENT= [('todo', 'Todo'), ('in_progress', 'In Progress'), ('done', 'Done')]

    title= models.CharField(max_length= 120)
    description= models.TextField()
    completed= models.BooleanField(default= False)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    priority= models.CharField(max_length=20, choices= PRIORITY_LEVEL, default= 'medium')
    status= models.CharField(max_length=20, choices= STATUS_CURRENT)    





