from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sales', views.sales, name='sales'),
    url(r'^items_list', views.items_list, name='items_list'),
    url(r'^items_edit/(?P<item>[a-z A-Z]{1,120})/$', views.items_edit, name='items_edit'),
    url(r'^items_add', views.items_add, name='items_add'),
    url(r'^sales', views.sales, name='sales'),
    url(r'^stats', views.stats, name='stats'),
    url(r'^reset', views.reset, name='reset'),
    url(r'^undo', views.undo, name='undo'),
]