from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def index(request):

    return render(request, 'index.html')
    
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(username=request.user).first()

    return render(request,'profile.html',{"profile":profile})

#view function that update the user's profile after log in
@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(username=request.user).first()

    # Allows users to view and update their profile
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=profile,files=request.FILES)

        # Saves data from the form to the profile table in the database
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()
        return redirect('home')
    else:
        form=ProfileForm()

    return render(request, 'update_profile.html',{"form":form, "profile":profile})

