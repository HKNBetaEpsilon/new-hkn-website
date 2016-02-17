from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import login
from utils import has_complete_profile, get_members_with_complete_profile, get_members_with_uncomplete_profile
from django.core.mail import send_mail, send_mass_mail

from users.models import Member
from electeeManagement.models import Electee
from users.forms import NewMemberForm
from hknWebsiteProject import settings
class MyError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

def home(request, bad_user = False):
	context = {}
	if not request.user.is_anonymous():
		# display prompt to ask member to complete their profile
		if not has_complete_profile(request.user.username):
			context = {
				'has_not_complete_profile' : True
			}

	elif bad_user:
		# Anonymous with an username:
		# The user tries to login but not a member
		context = {
			'not_member' : True
		}
	return render(request, "home.html", context)
	
def about(request):
	return render(request, "about.html", {})

def corporate(request):
	return render(request, "corporate.html", {})

def make_members(form, electee):
	context = {
		'error' : False
	}
	uniqnames = form.cleaned_data.get('new_members').split(',')
	try:
		# validate each submitted uniqname to make sure that a member 
		# 	with that uniqname does not alread exist, and that it is
		# 	alphabetic and a valid number of characters
		for name in uniqnames:
			if Member.objects.filter(uniqname = name).exists():
				raise MyError('Uniqname already exists')
	except MyError:
		context = {
			'error' : True,
			'error_msg' : 'Uniqname ' + name + ' alread exists!' 
		}
	else:
		# display message saying members were successfully submitted
		mail_list = []
		for name in uniqnames:	
			m = Member(uniqname = name)
			if electee:
				m.status = 'E'
			else:
				m.status = 'A'
			m.save()

			if electee:
				Electee(member = m).save()

			subject = '[HKN] Welcome to the HKN Beta Epsilon Website'
			message = welcome_msg
			from_email = settings.EMAIL_HOST_USER
			to_email = [name + '@umich.edu']
			mail_inst = (subject, message, from_email, to_email)
			mail_list.append(mail_inst)

		send_mass_mail(mail_list)
	return context

def create_new_members(request):
	context = {}

	form_electee = NewMemberForm(request.POST or None, prefix='electee')
	form_active = NewMemberForm(request.POST or None, prefix='active')

	if form_electee.is_valid():
		context = make_members(form_electee, True)
		form_electee = NewMemberForm()	
		if not context['error']:
			context['new_members_submitted'] = True

	if form_active.is_valid():
		context = make_members(form_active, False)
		form_active = NewMemberForm()	
		if not context['error']:
			context['new_members_submitted'] = True

	context['form_electee'] = form_electee
	context['form_active'] = form_active

	return render(request, "create_new_members.html", context)

def login_user(request):
	email = request.user.email
	email_base, provider = email.split('@')
	bad_user = False
	if not provider == 'umich.edu':
		request.user = badUser(request)
		bad_user = True
	else:
		try:
			m = Member.objects.get(uniqname = email_base)
			
			# If the user doesn't have name in thier profile, defualt to the 
			# name registered with their login info
			if not m.first_name:
				m.first_name = request.user.first_name
			if not m.last_name:
				m.last_name = request.user.last_name
			m.save()
		except Member.DoesNotExist:
			request.user = badUser(request)
			bad_user = True

	return home(request, bad_user)

def badUser(request):
	User.objects.get(username__exact=request.user).delete()
	return AnonymousUser()

welcome_msg = '''
Welcome to the HKN website! An account has been created for you.

Please go to hkn.eecs.umich.edu and log in with your umich account to complete your profile. Once you complete your profile, you will appear in the memeber list and you're resume will be included in the resume book.

Thanks,
HKN Website
'''

def awesome_actives(request):
	return render(request, "awesome_actives.html", {})

def misc_tools(request, success = False):
	total_num_users = Member.objects.count()
	num_members_comp_prof = get_members_with_complete_profile().count()
	context = {
		'success' : success,
		'total_num_users' : total_num_users,
		'num_members_comp_prof' : num_members_comp_prof
	}
	return render(request, "misc_tools.html", context)

def email_uncompleted_profiles(request):
	members_wo_profile = get_members_with_uncomplete_profile()
	mail_list = []

	for m in members_wo_profile:	
		subject = '[HKN] Reminder: Welcome to the HKN Beta Epsilon Website'
		message = 'Don\'t forget to complete your website profile!\n' + welcome_msg
		from_email = settings.EMAIL_HOST_USER
		to_email = [m.uniqname + '@umich.edu']
		# to_email = ['hkn.website@gmail.com']
		mail_inst = (subject, message, from_email, to_email)
		mail_list.append(mail_inst)

	send_mass_mail(mail_list)

	return misc_tools(request, True)