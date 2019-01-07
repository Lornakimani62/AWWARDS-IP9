from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$' ,views.index, name='home'),
    url(r'^update_profile/' ,views.update_profile, name='update'),
    url(r'^accounts/profile/',views.profile, name='profile'),
    url(r'^post_project/', views.post_project,name='new_project'),
    url(r'^search/', views.search, name='search')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)