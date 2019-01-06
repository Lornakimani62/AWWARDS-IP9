from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

#view function that displays the user's profile after log in
@login_required(login_url='/accounts/login/')
def profile(request):
    profile = Profile.objects.filter(username=request.user).first()

    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=profile,files=request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user

            profile.save()
        return redirect('Index')
    else:
        form=ProfileForm()
    return render(request, 'profile.html',{"form":form})

