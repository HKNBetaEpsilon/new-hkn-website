from django.shortcuts import render

# Create your views here.
from .models import Member
from electeeManagement.models import Electee, Requirements, Social, Service_Hours
from .forms import MemberForm
from .status import is_officer, is_electee
from hknWebsiteProject.resume_zip import zip_resumes
import string
from string import ascii_uppercase
import collections
from hknWebsiteProject.utils import get_members_with_complete_profile

def member_list(request):
	if request.user.is_anonymous():
		context = {
			'error' : True,
			'error_msg' : 'You must be a member to see member\'s profiles'
		}
	else :
		alpha_list = collections.OrderedDict()

		# displays the list of all members who have a complete profile
		members_with_completed_profile = get_members_with_complete_profile()

		# separate member list by letter first name starts with in order to display 
		# 	members in these groupings
		for letter in ascii_uppercase:
			member_list = members_with_completed_profile.filter(first_name__startswith=letter)
			member_list = member_list.order_by('first_name','last_name')
			if member_list:
				alpha_list[letter] = member_list

		context = {
			'member_list' : alpha_list,
			'error' : False,
		}

	return render(request, "member_list.html", context)


def profile(request, uniqname):
	context = {}

	if request.user.is_anonymous():
		context = {
			'error' : True,
			'error_msg' : 'You must be a member to see member\'s profiles'
		}
	else:
		is_curr_user = (request.user.username == uniqname)

		m = Member.objects.get(uniqname = uniqname)

		electee_progress = is_electee(uniqname) and (uniqname == request.user.username or is_officer(request.user.username))
		
		if electee_progress:
			e = Electee.objects.get(member_id = uniqname)
			requirements = dict ((requirements.requirement, requirements) for requirements in Requirements.objects.all())
			socials = Social.objects.filter(electee_id = uniqname)
			projects = Service_Hours.objects.filter(electee_id = uniqname)

			context = {
				'e' : e,
				'requirements' : requirements,
				'submit' : False,
				'socials' : socials,
				'projects' : projects
			}

			# if the request user is viewing their own electee progress, 
			# 	show the buttons to submit socials and service hours
			if (uniqname == request.user.username):
				context['submit'] = True

		context['profile'] = m
		context['is_curr_user'] = is_curr_user
		context['electee_progress'] = electee_progress
		context['error'] = False

	return render(request, "profile.html", context)

def profile_edit(request, uniqname):
	context = {}
	if request.user.is_anonymous() or uniqname != request.user.username:
		context = {
			'error' : True,
			'error_msg' : 'You cannot edit this profile'
		}
	else:
		context['profile_saved'] = False
		m = Member.objects.get(uniqname = uniqname)
		form = MemberForm(instance = m)	

		if request.POST:
			form = MemberForm(request.POST, request.FILES, instance = m)
			if form.is_valid():
				form.save()
				zip_resumes()
				context['profile_saved'] = True
				context['profile'] = m
				context['is_curr_user'] = 'is_curr_user'
				context['electee_progress'] = is_electee(uniqname) and (uniqname == request.user.username or is_officer(request.user.username))
		
				return render(request, "profile.html", context)

		context['form'] = form

	return render(request, "profile_edit.html", context)
