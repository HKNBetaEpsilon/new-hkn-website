from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.leadership, name='leadership'),
    url(r'^(?P<leader_saved>[0-1])/$', views.leadership, name='leadership'),
    url(r'^edit_leadership/(?P<position_added>[0-1])$', views.edit_leadership,
        name='edit_leadership'),
    url(r'^edit_leadership', views.edit_leadership, name='edit_leadership'),
    url(r'^add_leadership', views.add_leadership, name='add_leadership'),
    url(r'^delete_leader', views.delete_leader, name='delete_leader'),
]