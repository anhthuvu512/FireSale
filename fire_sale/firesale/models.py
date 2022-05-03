from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Seller(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

class Buyer(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=255)
    condition = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=9999)
    available = models.BooleanField(default=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
