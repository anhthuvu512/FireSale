from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from firesale.forms.item_form import ItemCreateForm, ItemUpdateForm
from firesale.models import Item, ItemImage, Seller


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        items = [{
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'firstImage': item.itemimage_set.first().image
        } for item in Item.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': items})
    context = {'items': Item.objects.all().order_by('name')}
    return render(request, 'sale/index.html', context)

def get_item_by_id(request, id):
    return render(request, 'sale/item_details.html', {
        'item': get_object_or_404(Item, pk=id)
    })

def sort_item(request):
    items = Item.objects.all()
    sort_by = request.GET.get('sort')
    if sort_by:
        items = items.order_by(sort_by)
    context = {'items': items}
    return render(request, 'sale/index.html', context)

@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
        for x in form:
            print(x.value())
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = Seller.objects.get(seller=request.user.id)
            item.save()
            item_image = ItemImage(image=request.POST['image'], item=item)
            item_image.save()
            return redirect('sale-index')
    else:
        form = ItemCreateForm()
    return render(request, 'sale/create_item.html', {
        'form': form
    })

@login_required
def update_item(request, id):
    instance = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        form = ItemUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('item-details', id=id)
    else:
        form = ItemUpdateForm(instance=instance)
    return render(request, 'sale/update_item.html', {
        'form': form,
        'id': id
    })

@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('sale-index')