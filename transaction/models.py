from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Transaction (models.Model):
    transaction_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    

    def __str__(self):
        return f"{self.transaction_date} - {self.description} (${self.amount})"

class User(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name