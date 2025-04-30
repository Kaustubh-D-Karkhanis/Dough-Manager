from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

@login_required
def dashboard(request):
    try:
        profile=request.user.userprofile
    except UserProfile.DoesNotExist:
        return redirect('setup_profile')
    return render(request, 'dashboard/home.html', {'profile':profile})

@login_required
def setup_profile(request):
    if request.method == 'POST':
        form=UserProfileForm(request.POST)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('dashboard')
    else:
        form=UserProfileForm()
    return render(request, 'dashboard/setup_profile.html', {'form':form})