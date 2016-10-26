from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^profile/(?P<uniqname>[a-z]{3,8})/$', views.profile, name='profile'),
    url(r'^update/(?P<uniqname>[a-z]{3,8})/$', views.profile_edit, name='profile_edit'),
    url(r'^member_list/$', views.member_list, name='member_list'),
]