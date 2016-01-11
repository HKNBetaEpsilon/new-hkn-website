from django.shortcuts import render

# Create your views here.

from .forms import SocialForm, ServiceHoursForm, RequirementsForm
from .models import Electee, Social, Service_Hours, Requirements
from users.status import is_officer, is_electee

# display all of the electee objects in a list, should only be viewable by officers
def all_electees(request):
	# get all of the electee objects to display
	electee_list = Electee.objects.filter(member__status='E')

	context = {
		'electee_list' : electee_list
	}

	return render(request, "all_electees.html", context)

def submit_social(request):
	# error if the request user is anonymous or not an electee
	if request.user.is_anonymous() or not is_electee(request.user.username):
		context = {
			'error' : True,
			'error_msg' : 'You must be an electee to submit socials'
		}
	else:
		context = {
			'error' : False,
			'social_submitted' : False
		}

		form = SocialForm(request.POST or None)
		if request.POST:
			if form.is_valid():
				social = form.save(commit=False)
				# set the electee field on the social model
				social.electee = Electee.objects.get(member_id = request.user.username)
				social.save()

				electee = Electee.objects.get(member_id = request.user.username)
				electee.num_socials_total = electee.num_socials_total + 1
				electee.save()

				# display a new blank form
				form = SocialForm(None)

				# show green bar at top of page saying that a social has been submitted
				context['social_submitted'] = True

		context['form'] = form

	return render(request, "submit_social.html", context)

def submit_service_hours(request):
	# error if the request user is anonymous or not an electee
	if request.user.is_anonymous() or not is_electee(request.user.username):
		context = {
			'error' : True,
			'error_msg' : 'You must be an electee to submit service hours'
		}
	else:
		context = {
			'error' : False,
			'service_hours_submitted' : False
		}

		form = ServiceHoursForm(request.POST or None)
		if request.POST:
			if form.is_valid():
				service_hours = form.save(commit=False)
				# set the electee field on the service_hours model
				service_hours.electee = Electee.objects.get(member_id = request.user.username)
				service_hours.save()

				electee = Electee.objects.get(member_id = request.user.username)
				electee.num_service_hours_total = electee.num_service_hours_total + service_hours.num_hours
				if service_hours.service_type == 'dB':
					electee.num_service_hours_db = electee.num_service_hours_db + service_hours.num_hours
				elif service_hours.service_type == 'HKN':
					electee.num_service_hours_hkn = electee.num_service_hours_hkn + service_hours.num_hours
				else:
					electee.num_service_hours_external = electee.num_service_hours_external + service_hours.num_hours
				electee.save()

				# display a new blank form
				form = ServiceHoursForm(None)

				# show green bar at top of page saying that a service hours have been submitted
				context['service_hours_submitted'] = True

		context['form'] = form

	return render(request, "submit_service_hours.html", context)

# shows a list of all unapporved socials and service hours
def electee_submission_approval(request):
	# get all unapproved socials and service hours
	social_list = Social.objects.filter(approved='0')
	service_hour_list = Service_Hours.objects.filter(approved='0')

	context = {
		'social_list' : social_list,
		'service_hour_list' : service_hour_list,
	}

	return render(request, "electee_submission_approval.html", context)

def edit_electee_requirements(request):
	context = {
		'requirement_changed' : False
	}

	form = RequirementsForm(request.POST or None)
	if form.is_valid():
		requirement = form.cleaned_data.get('requirement')
		num_required = form.cleaned_data.get('num_required')

		# change the current instance of this requirement to the new number of required hours
		instance = Requirements.objects.get(pk=requirement)
		instance.num_required = num_required
		instance.save()
		# display message saying that the requirement was successfully changed
		context['requirement_changed'] = True

	context['req_list'] = Requirements.objects.all().order_by('requirement')
	context['form'] = form

	return render(request, "edit_electee_requirements.html", context)

def initilize_electee_requirements(request):
	context = {
		'submitted' : False
	}

	if request.POST:
		a = Requirements(requirement = 'A_UG_SOCIAL', num_required = 0)
		a.save()
		b = Requirements(requirement = 'B_G_SOCIAL', num_required = 0)
		b.save()
		c = Requirements(requirement = 'C_UG_TOTAL_HOURS', num_required = 0)
		c.save()
		d = Requirements(requirement = 'D_G_TOTAL_HOURS', num_required = 0)
		d.save()
		e = Requirements(requirement = 'E_UG_DB_HOURS', num_required = 0)
		e.save()
		f = Requirements(requirement = 'F_G_DB_HOURS', num_required = 0)
		f.save()
		g = Requirements(requirement = 'G_UG_EXTERNAL_HOURS', num_required = 0)
		g.save()
		h = Requirements(requirement = 'H_G_EXTERNAL_HOURS', num_required = 0)
		h.save()
		i = Requirements(requirement = 'I_SINGLE_SERVICE_EVENT_HOURS', num_required = 0)
		i.save()

		context['submitted'] = True

	return render(request, "initilize_electee_requirements.html", context)