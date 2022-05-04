from django.forms import ModelForm, widgets
from django import forms
from firesale.models import Item

class ItemCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Item
        exclude = ['id', 'highest_offer', 'available']
        fields = ['name','condition','description','seller']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'seller': widgets.Select(attrs={'class': 'form-control'})
        }

class ItemUpdateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Item
        exclude = ['id', 'highest_offer', 'available']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'seller': widgets.Select(attrs={'class': 'form-control'})
        }