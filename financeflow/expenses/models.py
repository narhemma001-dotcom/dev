from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=20, choices=[("food","Food"), ("transportation", "Transportation"),("shopping", "Shopping"),("entertainment", "Entertainment"), ("bills", "Bills")])
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    color= models.CharField(max_length=20 ,blank=True, null=True)

    def __str__(self):
        return self.get_name_display()

class Expense(models.Model):
    amount= models.DecimalField(max_digits=10, decimal_places= 2)
    category= models.ForeignKey(Category, on_delete=models.SET_NULL, null= True, blank= True)
    date= models.DateField(blank=True, null=True)
    description= models.TextField()   
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - ${self.amount}"
