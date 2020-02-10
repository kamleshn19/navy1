from django.db import models

# Create your models here.
class issueTable(models.Model):
    partNo = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    loggedBy = models.CharField(max_length=20)