from django.db import models

# Create your models here.
class Signupc(models.Model):
    username=models.CharField(max_length=122)
    email=models.EmailField(max_length=122)
    No = models.IntegerField()
    password=models.CharField(max_length=122)
    password_repeat = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.username
class Donatec(models.Model):
    namet=models.CharField(max_length=122)
    location=models.CharField(max_length=122)
    food=models.CharField(max_length=122)
    hour=models.IntegerField()
    quantit=models.IntegerField()
    

    