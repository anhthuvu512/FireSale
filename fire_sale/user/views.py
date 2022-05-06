from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from user.models import Profile, Address, Payment
from user.forms.user_form import ProfileForm, UserContactForm, UserPaymentForm

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
    return render(request, 'user/profile.html', {
        'user': get_object_or_404(Profile)
    })

@login_required
def edit_profile(request):
    instance = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=instance, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('sale-index')
    return render(request, 'user/edit_profile.html', {
        'form': ProfileForm(instance=instance)
    })

@login_required
def contact(request):
    instance = Address.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = UserContactForm(instance=instance, data=request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('payment')
    return render(request, 'user/contact.html', {
        'form': UserContactForm()
    })

@login_required
def payment(request):
    instance = Payment.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = UserPaymentForm(instance=instance, data=request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            print(payment)
            return redirect('sale-index')
    return render(request, 'user/payment.html', {
        'form': UserPaymentForm()
    })






























