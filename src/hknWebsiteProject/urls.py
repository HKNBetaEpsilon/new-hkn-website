"""hknWebsiteProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Import the include() function: from django.conf.urls import url, include
	3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^$', 'hknWebsiteProject.views.home', name='home'),
	url(r'^admin/', admin.site.urls),  
	url(r'^members/', 'users.views.member_list', name='member_list'),
	url(r'^about/', 'hknWebsiteProject.views.about', name='about'),
	url(r'^corporate/', 'hknWebsiteProject.views.corporate', name='corporate'),
	url(r'^create_new_members/', 'hknWebsiteProject.views.create_new_members', name='create_new_members'),
	url(r'^edit_electee_requirements/', 'hknWebsiteProject.views.edit_electee_requirements', name='edit_electee_requirements'),
	url(r'^all_electees/', 'users.views.all_electees', name='all_electees'),
	url(r'^login_user/', 'hknWebsiteProject.views.login_user', name='login_user'), 
	url(r'^profile/(?P<uniqname>[a-z]{3,8})/$', 'users.views.profile', name='profile'),
	url(r'^update/(?P<uniqname>[a-z]{3,8})/$', 'users.views.profile_edit', name='profile_edit'),
	url(r'^electee_progress/(?P<uniqname>[a-z]{3,8})/$', 'users.views.electee_progress', name='electee_progress'),
	url(r'^submit_social/', 'users.views.submit_social', name='submit_social'),
	url(r'^submit_service_hours/', 'users.views.submit_service_hours', name='submit_service_hours'),
	url(r'^electee_submission_approval/', 'users.views.electee_submission_approval', name='electee_submission_approval'),
	url(r'^leadership/(?P<leader_saved>[0-1])/$', 'leadership.views.leadership', name='leadership'),
	url(r'^leadership/', 'leadership.views.leadership', name='leadership'),
	url(r'^edit_leadership/(?P<position_added>[0-1])/$', 'leadership.views.edit_leadership', name='edit_leadership'),
	url(r'^edit_leadership/', 'leadership.views.edit_leadership', name='edit_leadership'),
	url(r'^add_leadership/', 'leadership.views.add_leadership', name='add_leadership'),
	url(r'^delete_leader/', 'leadership.views.delete_leader', name='delete_leader'),

	url('', include('social.apps.django_app.urls', namespace='social')),
	url('', include('django.contrib.auth.urls', namespace='auth')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)