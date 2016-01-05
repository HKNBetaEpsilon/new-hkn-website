from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import login
from utils import has_complete_profile

from users.models import Member, Electee
from users.forms import NewMemberForm
from electeeManagement.models import Requirements
from electeeManagement.forms import RequirementsForm

class MyError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

def home(request):
	context = {}
	if not request.user.is_anonymous():
		if not has_complete_profile(request.user.username):
			context = {
				'has_not_complete_profile' : True
			}
	return render(request, "home.html", context)

def about(request):
	return render(request, "about.html", {})

def corporate(request):
	return render(request, "corporate.html", {})

def tools(request):
	context = {}
	context['new_members_submitted'] = False

	form = NewMemberForm(request.POST or None)
	if form.is_valid():
		uniqnames = form.cleaned_data.get('new_members').split(',')
		try:
			for name in uniqnames:
				if Member.objects.filter(uniqname = name).exists():
					raise MyError('Uniqname already exists')
				else:
					m = Member(uniqname = name)
					m.save()
					Electee(member = m).save()
		except MyError:
			context = {
				'error' : True,
				'error_msg' : 'Uniqname ' + name + ' alread exists!' 
			}
		else:
			context['new_members_submitted'] = True
	
	context['form'] = form

	return render(request, "tools.html", context)

def tools2(request):
	context = {
		'requirement_changed' : False
	}

	form = RequirementsForm(request.POST or None)
	if form.is_valid():
		requirement = form.cleaned_data.get('requirement')
		num_required = form.cleaned_data.get('num_required')

		instance = Requirements.objects.get(pk=requirement)
		instance.num_required = num_required
		instance.save()
		context['requirement_changed'] = True

	context['req_list'] = Requirements.objects.all().order_by('requirement')
	context['form'] = form

	return render(request, "tools2.html", context)

def login_user(request):
	email = request.user.email
	email_base, provider = email.split('@')
	if not provider == 'umich.edu':
		request = badUser(request)
	else:
		try:
			m = Member.objects.get(uniqname = email_base)
		except Member.DoesNotExist:
			request = badUser(request)

	return redirect('/')

def badUser(request):
	User.objects.get(username__exact=request.user).delete()
	return AnonymousUser()