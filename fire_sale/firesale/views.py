from django.shortcuts import render, get_object_or_404, redirect
from firesale.forms.item_form import ItemCreateForm
from firesale.models import Item, ItemImage


# Create your views here.
def index(request):
    context = {'items': Item.objects.all().order_by('name')}
    return render(request, 'sale/index.html', context)

def get_item_by_id(request, id):
    return render(request, 'sale/item_details.html', {
        'item': get_object_or_404(Item, pk=id)
    })

def create_item(request):
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = form.save()
            item_image = ItemImage(image=request.POST['image'], item=item)
            item_image.save()
            return redirect('sale-index')
    else:
        form = ItemCreateForm()
    return render(request, 'sale/create_item.html', {
        'form': form
    })