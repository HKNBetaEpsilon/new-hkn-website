from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^edit_electee_requirements', views.edit_electee_requirements,
        name='edit_electee_requirements'),
    url(r'^all_electees', views.all_electees, name='all_electees'),
    url(r'^submit_social', views.submit_social, name='submit_social'),
    url(r'^submit_service_hours', views.submit_service_hours,
        name='submit_service_hours'),
    url(r'^electee_submission_approval/(?P<approved>[0-1])$',
        views.electee_submission_approval, name='electee_submission_approval'),
    url(r'^electee_submission_approval', views.electee_submission_approval,
        name='electee_submission_approval'),
    url(r'^initilize_electee_requirements',
        views.initilize_electee_requirements,
        name='initilize_electee_requirements'),
    url(r'^electee_turn_ins', views.electee_turn_ins, name='electee_turn_ins'),
    url(r'^electee_convert/(?P<uniqname>[a-z]{3,8})$', views.convert,
        name='electee_convert'),
    url(r'^electee_remove/(?P<uniqname>[a-z]{3,8})$', views.remove_electee,
        name='electee_remove'),
]