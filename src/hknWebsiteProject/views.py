from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import login

from users.models import Member
from users.forms import NewMemberForm

def home(request):
	return render(request, "home.html", {})

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
		for name in uniqnames:
			Member(uniqname = name).save()
		context['new_members_submitted'] = True
	
	context['form'] = form

	return render(request, "tools.html", context)

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