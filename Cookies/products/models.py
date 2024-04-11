from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    comment = models.TextField()
    tags = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='photos/')


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    
# Create your models here.
