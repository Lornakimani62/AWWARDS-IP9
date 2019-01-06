from django.test import TestCase
from .models import *

# Tests the profile methods 
class ProfileTestClass(TestCase):

    '''test for profile
        '''
    
    def setUp(self):
        #initial instance to run at the begginning of every test
        self.username = User.objects.create_user('lorna','pas123')
        self.new_profile = Profile(description='Test',avatar='',username=self.username,email='kimanilorna@yahoo.com')
    
    def tearDown(self):
        """ Runs after each profile test case
            """
    def test_init(self):
        """ Test whether objects are initialized properly 
            """

        self.assertEqual(self.new_profile.description, "Test")
        self.assertEqual(self.new_profile.username, self.username)
        self.assertEqual(self.new_profile.avatar, '')
        self.assertEqual(self.new_profile.email, 'kimanilorna@yahoo.com')


    def test_save_profile(self):
        """ test whether new profile is added to Accounts list 
            """

        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

class ProjectTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_profile = Profile(username=self.new_user)
        self.new_profile.save()
        self.new_project = Project(id=1,image='photos/photo',title='Test Project',description='Test Description',username=self.new_user,link='http://livesite.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_project(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_project(self):
        self.new_project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)