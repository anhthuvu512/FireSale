from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from user.models import Profile
from user.forms.profile_form import ProfileForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })

def profile(request):
    return render(request, 'user/profile.html', {
        'user': get_object_or_404(Profile)
    })

def edit_profile(request):
    instance = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=instance, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/edit_profile.html', {
        'form': ProfileForm(instance=instance)
    })































