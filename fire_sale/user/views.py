from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Avg
from django.shortcuts import render, get_object_or_404, redirect
from user.models import Profile, Address, Payment, Rating
from firesale.models import Item, Seller, Buyer, Offer, SellerNotification, BuyerNotification
from user.forms.user_form import ProfileForm, UserContactForm, UserPaymentForm, UserRatingForm

seller_notifs = SellerNotification.objects.all()
buyer_notifs = BuyerNotification.objects.all()

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })

@login_required
def profile(request):
    instance = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('sale-index')
    ratings = Rating.objects.filter(seller=Seller.objects.get(seller=request.user.id)).aggregate(Avg('rate'))
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=instance),
        'seller_notifs': seller_notifs.order_by('-id'),
        'buyer_notifs': buyer_notifs.order_by('-id'),
        'ratings': ratings
    })

@login_required
def contact(request, id):
    instance = Address.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = UserContactForm(instance=instance, data=request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('payment', id=id)
    ratings = Rating.objects.filter(seller=Seller.objects.get(seller=request.user.id)).aggregate(Avg('rate'))
    return render(request, 'user/contact.html', {
        'form': UserContactForm(instance=instance),
        'id': id,
        'offer': Offer.objects.get(pk=id),
        'seller_notifs': seller_notifs.order_by('-id'),
        'buyer_notifs': buyer_notifs.order_by('-id'),
        'ratings': ratings
    })

@login_required
def payment(request, id):
    instance = Payment.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = UserPaymentForm(instance=instance, data=request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            return redirect('rate-seller', id=id)
    return render(request, 'user/payment.html', {
        'form': UserPaymentForm(instance=instance),
        'id': id,
        'offer': Offer.objects.get(pk=id),
        'seller_notifs': seller_notifs.order_by('-id'),
        'buyer_notifs': buyer_notifs.order_by('-id'),
        'ratings': Rating.objects.filter(seller=Seller.objects.get(seller=request.user.id)).aggregate(Avg('rate'))
    })

@login_required
def rate_seller(request, id):
    seller = Seller.objects.get(pk=Offer.objects.get(pk=id).seller.id)
    item = Item.objects.get(pk=Offer.objects.get(pk=id).item.id)
    instance = Rating.objects.filter(item=item).first()
    if request.method == 'POST':
        form = UserRatingForm(instance=instance,data=request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            if rating.rate:
                rating.seller = seller
                rating.item = item
            rating.save()
            return redirect('review', id=id)
    return render(request, 'user/rate_seller.html', {
        'form': UserRatingForm(instance=instance),
        'id': id,
        'offer': Offer.objects.get(pk=id),
        'seller_notifs': seller_notifs.order_by('-id'),
        'buyer_notifs': buyer_notifs.order_by('-id'),
        'ratings': Rating.objects.filter(seller=Seller.objects.get(seller=request.user.id)).aggregate(Avg('rate'))
    })

@login_required
def review(request, id):
    return render(request, 'user/review.html', {
        'item': get_object_or_404(Item, pk=Offer.objects.get(pk=id).item.id),
        'contact': get_object_or_404(Address, user=request.user.id),
        'payment': get_object_or_404(Payment, user=request.user.id),
        'id': id,
        'offer': Offer.objects.get(pk=id),
        'seller_notifs': seller_notifs.order_by('-id'),
        'buyer_notifs': buyer_notifs.order_by('-id'),
        'ratings': Rating.objects.filter(seller=Seller.objects.get(seller=request.user.id)).aggregate(Avg('rate'))
    })






























