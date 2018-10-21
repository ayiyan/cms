from django.db import models

# Create your models here.

class ServerManagent(models.Model):
    classnum = models.CharField(max_length=5)
    provider = models.CharField(max_length=5)
    service = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    area = models.CharField(max_length=10)
    system = models.CharField(max_length=15)
    outside = models.CharField(max_length=15)
    inside = models.CharField(max_length=15)
    cpu = models.CharField(max_length=55)
    memory = models.CharField(max_length=3)
    disk = models.CharField(max_length=10)
    date = models.DateField()
    status = models.CharField(max_length=5)
    def __str__(self):
        return self.name
