from django.forms import ModelForm, widgets
from django import forms
from firesale.models import *

class ItemCreateForm(ModelForm):
    images = forms.FileField(required=True)
    class Meta:
        model = Item
        exclude = ['id', 'highest_offer', 'available', 'seller']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
        }

class ItemUpdateForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['id', 'highest_offer', 'available', 'seller']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
        }

class ItemImageAddForm(ModelForm):
    class Meta:
        model = ItemImage
        exclude = ['id', 'item']

class MakeOfferForm(ModelForm):
    class Meta:
        model = Offer
        exclude = ['id', 'accepted', 'buyer', 'item', 'seller']
        widgets = {
            'price': widgets.TextInput(attrs={'class': 'form-control'}),
            'message': widgets.TextInput(attrs={'class': 'form-control'})
        }

class Seller_Notif(ModelForm):
    class Meta:
        model = SellerNotification
        exclude = ['id', 'receiver', 'sender']
        widgets = {
            'notif': forms.Select(attrs={'class': 'form-control'})
        }