from django.db import models

# Create your models here.


class Review(models.Model):
    user_name=models.CharField(max_length=100) #logic is to remove max_length but needed for db configuration
    review_text=models.TextField()
    rating=models.IntegerField()
    