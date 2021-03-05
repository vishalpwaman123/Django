from django.db import models

class sqlserverconnection(models.Model): 
    Empid = models.IntegerField()
    Empname=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Salary=models.IntegerField()


class Insertdata(models.Model):
    Empname=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Salary=models.IntegerField()