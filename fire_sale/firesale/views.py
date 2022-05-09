from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from firesale.forms.item_form import ItemCreateForm, ItemUpdateForm, MakeOfferForm
from firesale.models import *


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
    notifs = SellerNotification.objects.all()
    context = {'items': Item.objects.all().order_by('name'),'notifs': notifs}
    return render(request, 'sale/index.html', context)

def item_details(request, id):
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

@login_required
def make_offer(request, id):
    if request.method == 'POST':
        form = MakeOfferForm(data=request.POST)
        for x in form:
            print(x.value())
        if form.is_valid():
            offer = form.save(commit=False)
            offer.buyer = Buyer.objects.get(buyer=request.user.id)
            offer.item = Item.objects.get(pk=id)
            offer.save()
            notification = SellerNotification.objects.create(sender=offer.buyer,
                                                             receiver=offer.item.seller,
                                                             notif=str(request.user.username)+' offers '+str(offer.price)+'kr for '+str(offer.item.name))
            notification.save()
            return redirect('sale-index')
    else:
        form = MakeOfferForm()
    return render(request, 'sale/make_offer.html', {
        'form': form,
        'id': id
    })

@login_required
def seller_notif_detail(request, id):
    notif=SellerNotification.objects.get(pk=id)
    offer=Offer.objects.get(buyer_id=notif.sender.id)
    item = Item.objects.get(pk=offer.item.id)
    item_img=ItemImage.objects.get(item=item.id)
    return render(request, 'sale/notification_detail.html', {
        'notif': notif,
        'offer': offer,
        'item': item,
        'item_img': item_img
    })