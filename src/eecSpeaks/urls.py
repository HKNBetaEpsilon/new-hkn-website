from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^blog/(?P<blogid>[0-9]*)$', views.view_post),
    url(r'blog/(?P<blogid>[0-9]*)/edit', views.edit_post),
    url(r'^post', views.add_blogpost, name='post'),
    url(r'', views.show_blogposts, name='eecspeaks')
]