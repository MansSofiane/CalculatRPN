from django.db import models

class Stack(models.Model): 
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, blank=True, null= True) 


class operation(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField() 
    stack = models.ForeignKey(Stack, on_delete=models.CASCADE)
