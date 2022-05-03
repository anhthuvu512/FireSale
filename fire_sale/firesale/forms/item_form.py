from django.forms import ModelForm, widgets
from django import forms
from firesale.models import Item

class ItemCreateForm(ModelForm):
    image: forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Item
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'highest_offer': widgets.NumberInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'available': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'seller': widgets.Select(attrs={'class': 'form-control'})
        }