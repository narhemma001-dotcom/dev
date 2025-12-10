from django.db import models

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length= 255)
    description= models.TextField()
    technologies= models.CharField(max_length=255)
    project_url= models.CharField(max_length=255)
    github_url= models.CharField(max_length=255)
    image= models.ImageField(blank= True, null=True)
    date_added= models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return self.title