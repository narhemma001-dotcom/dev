from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=255)
    slug= models.SlugField(max_length=255, unique= True)
    content= models.TextField(blank= True, null= True)
    excerpt= models.TextField(blank= True, null= True)
    feature_image= models.ImageField(upload_to='blog_images/', blank= True, null=True)
    date_created= models.DateTimeField(auto_now_add= True)
    date_updated= models.DateTimeField(auto_now= True)
    published_status= models.BooleanField(default=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug or "": 
            self.slug = slugify(self.title)
        super().save(*args, **kwargs) 