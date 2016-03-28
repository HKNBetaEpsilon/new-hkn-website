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
	url(r'^edit_electee_requirements/', 'electeeManagement.views.edit_electee_requirements', name='edit_electee_requirements'),
	url(r'^all_electees/', 'electeeManagement.views.all_electees', name='all_electees'),
	url(r'^login_user/', 'hknWebsiteProject.views.login_user', name='login_user'), 
	url(r'^profile/(?P<uniqname>[a-z]{3,8})/(?P<profile_saved>[0-1])/$', 'users.views.profile', name='profile'),
	url(r'^profile/(?P<uniqname>[a-z]{3,8})/$', 'users.views.profile', name='profile'),
	url(r'^update/(?P<uniqname>[a-z]{3,8})/$', 'users.views.profile_edit', name='profile_edit'),
	url(r'^submit_social/', 'electeeManagement.views.submit_social', name='submit_social'),
	url(r'^submit_service_hours/', 'electeeManagement.views.submit_service_hours', name='submit_service_hours'),
	url(r'^electee_submission_approval/(?P<approved>[0-1])$', 'electeeManagement.views.electee_submission_approval', name='electee_submission_approval'),
	url(r'^electee_submission_approval/', 'electeeManagement.views.electee_submission_approval', name='electee_submission_approval'),
	url(r'^leadership/(?P<leader_saved>[0-1])/$', 'leadership.views.leadership', name='leadership'),
	url(r'^leadership/', 'leadership.views.leadership', name='leadership'),
	url(r'^edit_leadership/(?P<position_added>[0-1])/$', 'leadership.views.edit_leadership', name='edit_leadership'),
	url(r'^edit_leadership/', 'leadership.views.edit_leadership', name='edit_leadership'),
	url(r'^add_leadership/', 'leadership.views.add_leadership', name='add_leadership'),
	url(r'^delete_leader/', 'leadership.views.delete_leader', name='delete_leader'),
	url(r'^initilize_electee_requirements/', 'electeeManagement.views.initilize_electee_requirements', name='initilize_electee_requirements'),
	url(r'^electee_turn_ins/', 'electeeManagement.views.electee_turn_ins', name='electee_turn_ins'),
	url(r'^db_cafe/items_list', 'dbcafe.views.items_list', name='items_list'),
	url(r'^db_cafe/items_edit/(?P<item>[a-z A-Z]{1,120})/$', 'dbcafe.views.items_edit', name='items_edit'),
	url(r'^db_cafe/items_add', 'dbcafe.views.items_add', name='items_add'),
	url(r'^db_cafe/sales', 'dbcafe.views.sales', name='sales'),
	url(r'^db_cafe/stats', 'dbcafe.views.stats', name='stats'),
	url(r'^db_cafe/reset', 'dbcafe.views.reset', name='reset'),
	url(r'^db_cafe/undo', 'dbcafe.views.undo', name='undo'),
	url(r'^/awesome_actives', 'hknWebsiteProject.views.awesome_actives', name='awesome_actives'),
	url(r'^/misc_tools/(?P<success>[0-1])/$', 'hknWebsiteProject.views.misc_tools', name='misc_tools'),
	url(r'^/misc_tools', 'hknWebsiteProject.views.misc_tools', name='misc_tools'),
	url(r'^/email_uncompleted_profiles', 'hknWebsiteProject.views.email_uncompleted_profiles', name='email_uncompleted_profiles'),
	url(r'^/make_alumni', 'hknWebsiteProject.views.make_alumni', name='make_alumni'),
	url('', include('social.apps.django_app.urls', namespace='social')),
	url('', include('django.contrib.auth.urls', namespace='auth')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)