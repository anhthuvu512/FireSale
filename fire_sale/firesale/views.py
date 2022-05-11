from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from firesale.forms.item_form import *
from firesale.models import *
from user.models import *

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
    ratings =  Rating.objects.filter(seller=Seller.objects.get(seller=request.user.id)).aggregate(Avg('rate'))
    seller_notifs = SellerNotification.objects.all()
    buyer_notifs = BuyerNotification.objects.all()
    context = {'items': Item.objects.all().order_by('name'),
               'seller_notifs': seller_notifs.order_by('-id'),
               'buyer_notifs': buyer_notifs.order_by('-id'),
               'ratings': ratings}
    return render(request, 'sale/index.html', context)

def item_details(request, id):
    item = get_object_or_404(Item, pk=id)
    similar_items = []
    for partial_name in item.name.split():
        similar_item = Item.objects.filter(name__icontains=partial_name)
        similar_items+=similar_item
    similar_items = list(dict.fromkeys(similar_items))
    for similar_item in similar_items:
        if similar_item == item:
            similar_items.remove(similar_item)
    return render(request, 'sale/item_details.html', {
        'item': item,
        'similar_items': similar_items
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
def add_image(request, id):
    if request.method == 'POST':
        form = ItemImageAddForm(data=request.POST)
        if form.is_valid():
            item_img = form.save(commit=False)
            item_img.item = Item.objects.get(pk=id)
            item_img.save()
            return redirect('item-details', id=id)
    else:
        form = ItemImageAddForm()
    return render(request, 'sale/add_image.html', {
        'form': form,
        'id': id
    })

@login_required
def make_offer(request, id):
    if request.method == 'POST':
        form = MakeOfferForm(data=request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.buyer = Buyer.objects.get(buyer=request.user.id)
            offer.item = Item.objects.get(pk=id)
            offer.seller = Seller.objects.get(pk=Item.objects.get(pk=id).seller.id)
            offer.save()
            notification = SellerNotification.objects.create(sender=offer.buyer,
                                                             receiver=offer.item.seller,
                                                             offer_id=offer.id,
                                                             notif=str(request.user.username)+' offers '+str(offer.price)+
                                                                   'kr for '+str(offer.item.name))
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
    notif = SellerNotification.objects.get(pk=id)
    offer = Offer.objects.get(pk=notif.offer_id)
    item = Item.objects.get(pk=offer.item_id)
    return render(request, 'sale/view_offer.html', {
        'notif': notif,
        'offer': offer,
        'item': item
    })

@login_required
def decline_offer(request, id):
    notif = SellerNotification.objects.get(pk=id)
    offer = Offer.objects.get(pk=notif.offer_id)
    notification = BuyerNotification.objects.create(sender_id=notif.receiver_id,
                                                    receiver=offer.buyer,
                                                    offer_id=offer.id,
                                                    notif=str(request.user.username) + ' rejects the offer ' +
                                                           str(offer.price) + 'kr for ' + str(offer.item.name))
    notification.save()
    notif.delete()
    return redirect('sale-index')


@login_required
def accept_offer(request, id):
    notif = SellerNotification.objects.get(pk=id)
    offer = Offer.objects.get(pk=notif.offer_id)
    notification = BuyerNotification.objects.create(sender_id=notif.receiver_id,
                                                    receiver=offer.buyer,
                                                    offer_id=offer.id,
                                                    notif=str(request.user.username) + ' accepts the offer ' +
                                                          str(offer.price) + 'kr for ' + str(offer.item.name))
    notification.save()
    notif.delete()
    offer.accepted = True
    offer.save()
    return redirect('sale-index')