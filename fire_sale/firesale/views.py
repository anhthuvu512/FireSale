from django.shortcuts import render
from fire_sale.firesale.models import User

items = [
    {'name': 'notebook', 'offer': 4.99},
    {'name': 'journal', 'offer': 6.99},
    {'name': 'pen', 'offer': 0.99}
]

# Create your views here.
def index(request):
    User.objects.filter(name__icontains=)
    return render(request, 'sale/index.html', context={'items': items})