from django.db import models

# Create your models here.

class Students(models.Model):
    sid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    password=models.IntegerField()
