from django.db import models

# Create your models here.
class Receipt(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    ingredients = models.TextField()
    directions = models.TextField()
    