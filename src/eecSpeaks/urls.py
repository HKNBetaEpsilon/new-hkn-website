from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^blog/(?P<blogid>[0-9]*)$', views.view_post),
    url(r'^addblogpost', views.add_blogpost, name='addblogpost'),
    url(r'', views.show_blogposts, name='eecspeaks')
]