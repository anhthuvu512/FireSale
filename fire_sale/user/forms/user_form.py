from django.forms import ModelForm, widgets
from django_countries.widgets import CountrySelectWidget
from user.models import Profile, Address, Payment, Rating

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'}),
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'bio': widgets.TextInput(attrs={'class': 'form-control'})
        }

class UserContactForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['id', 'user']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_nr': widgets.NumberInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
            'country': CountrySelectWidget(attrs={'class': 'form-control'})
        }

class UserPaymentForm(ModelForm):
    class Meta:
        model = Payment
        exclude = ['id', 'user']
        widgets = {
            'cardholder': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_nr': widgets.NumberInput(attrs={'class': 'form-control'}),
            'expiry_date': widgets.DateInput(attrs={'class': 'form-control'}, format='%m/%y'),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'})
        }

class UserRatingForm(ModelForm):
    class Meta:
        model = Rating
        exclude = ['id', 'seller']
        widgets = {
            'rate': widgets.NumberInput(attrs={'class': 'form-control'})
        }
