from django.forms import ModelForm, widgets
from django import forms
from firesale.models import Item, Offer

class ItemCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
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

class MakeOfferForm(ModelForm):
    class Meta:
        model = Offer
        exclude = ['id', 'accepted', 'buyer', 'item']
        widgets = {
            'price': widgets.TextInput(attrs={'class': 'form-control'}),
            'message': widgets.TextInput(attrs={'class': 'form-control'})
        }