from django.shortcuts import render, get_object_or_404
from firesale.models import Item

# Create your views here.
def index(request):
    context = {'items': Item.objects.all().order_by('name')}
    return render(request, 'sale/index.html', context)

def get_item_by_id(request, id):
    return render(request, 'sale/item_details.html', {
        'item': get_object_or_404(Item, pk=id)
    })