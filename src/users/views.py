from django.shortcuts import render

# Create your views here.
from .models import Member
from .forms import MemberForm
import string

def member_list(request):
	member_list = Member.objects.all().filter(first_name__isnull=False).filter(last_name__isnull=False)
	member_list = member_list.exclude(first_name__exact="").exclude(last_name__exact="")
	member_list = member_list.order_by('first_name','last_name')

	context = {
		'member_list' : member_list
	}

	return render(request, "member_list.html", context)


def profile(request, uniqname):
	if request.user.is_anonymous():
		context = {
			'error' : True,
			'error_msg' : 'You must be a member to see member\'s profiles'
		}
	else:
		is_curr_user = (request.user.username == uniqname)

		m = Member.objects.get(uniqname = uniqname)
		
		context = {
			'profile': m,
			'is_curr_user': is_curr_user,
			'error' : False,
		}

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
				context['profile_saved'] = True

		context['uniqname'] = uniqname
		context['form'] = form

	return render(request, "profile_edit.html", context)
