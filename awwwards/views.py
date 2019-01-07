from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.urls import reverse
from django.db.models import Max,F

def index(request):
    projects = Project.objects.all() # retrieves  projects from the database
    best_rating = 0
    best_project = Project.objects.annotate(max=Max(F('content')+ F('design')+ F('usability'))).order_by('-max').first() # finds the project with the highest rates
    
    # calculates the most rated project by looping through all of them to get average
    for project in projects:
        average = (project.design + project.usability + project.content)/3
        best_rating = round(average,2)
    return render(request,'index.html',{'projects':projects,'best_rating':best_rating,'best_project':best_project})

#view function that view the user's profile after log in
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

    # Allows users to update their profile
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


@login_required(login_url='/accounts/login/')
def post_project(request):
    current_user = request.user

    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = project = Project(title=request.POST['title'],image=request.FILES['image'],description=request.POST['description'],link=request.POST['link'],username=request.user)
            project.save()
        return redirect('home')
    else:
        form = ProjectForm()

    return render(request,'post_project.html',{"form":form})



@login_required(login_url='/accounts/login/')
def search(request):
    current_user = request.user
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.find_project(search_term)
        message=f"{search_term}"


        return render(request,'search.html',{"message":message,"projects":searched_projects,"profile":profile})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def project(request,project_id):
    project = Project.objects.get(id=project_id)
    rating = round(((project.design + project.usability + project.content)/3),2)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            project.vote_submissions += 1
            if project.design == 0:
                project.design = int(request.POST['design'])
            else:
                project.design = (project.design + int(request.POST['design']))/2
            if project.usability == 0:
                project.usability = int(request.POST['usability'])
            else:
                project.usability = (project.design + int(request.POST['usability']))/2
            if project.content == 0:
                project.content = int(request.POST['content'])
            else:
                project.content = (project.design + int(request.POST['content']))/2
            project.save()
            return redirect(reverse('project',args=[project.id]))
    else:
        form = VoteForm()
    return render(request,'project.html',{'form':form,'project':project,'rating':rating})