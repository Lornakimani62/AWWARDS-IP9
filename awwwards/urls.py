from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$' ,views.index, name='home'),
    url(r'^update_profile/' ,views.update_profile, name='update'),
    url(r'^accounts/profile/',views.profile, name='profile'),
    url(r'^post_project/', views.post_project,name='new_project'),
]