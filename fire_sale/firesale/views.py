from django.shortcuts import render

items = [
    {'name': 'notebook', 'offer': 4.99},
    {'name': 'journal', 'offer': 5.99},
    {'name': 'pen', 'offer': 0.99}
]

# Create your views here.
def index(request):
    return render(request, 'sale/index.html', context={'items': items})