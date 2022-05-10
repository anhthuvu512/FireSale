from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from firesale.models import Seller, Item

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_nr = models.IntegerField()
    city = models.CharField(max_length=255)
    zip = models.IntegerField()
    country = CountryField()

class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cardholder = models.CharField(max_length=255)
    card_nr = models.CharField(max_length=255)
    expiry_date = models.DateField()
    cvc = models.IntegerField()

class Rating(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self):
        return str(self.rate)