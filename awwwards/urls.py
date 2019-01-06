from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$' ,views.index, name='home'),
    url(r'^accounts/profile',views.profile, name='profile'),
]