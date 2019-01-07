from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from url_or_relative_url_field.fields import URLOrRelativeURLField


class Profile(models.Model):
    '''A class to allow users to update and view their profile
        '''
    avatar = models.ImageField(upload_to='media/')
    description = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    project = models.ForeignKey('Project',on_delete=models.CASCADE,null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username


class Project(models.Model):
    '''A class that allows users to post,view and rate projects
        '''
    
    title = models.CharField(max_length=20)
    description = HTMLField()
    image = models.ImageField(upload_to='media/')
    link = URLOrRelativeURLField()
    username =  username = models.ForeignKey(User,on_delete=models.CASCADE)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    vote_submissions = models.IntegerField(default=0)


    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def find_project(cls, search_term):
        projects = cls.objects.filter(project__title__icontains=search_term)
        return projects

    def __str__(self):
        return self.title