from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Seller(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.seller)

class Buyer(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.buyer)

class Item(models.Model):
    name = models.CharField(max_length=255)
    highest_offer = models.IntegerField(blank=True, default=0)
    condition = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    available = models.BooleanField(blank=True, default=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ItemImage(models.Model):
    image = models.CharField(max_length=9999)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.image

class Offer(models.Model):
    price = models.IntegerField()
    accepted = models.BooleanField(default=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.price)