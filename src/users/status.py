from django.conf import settings
from users.models import Member

def is_officer(uniqname):
	m = Member.objects.get(uniqname = uniqname)
	return m.status == 'O'

def is_electee(uniqname):
	m = Member.objects.get(uniqname = uniqname)
	return m.status == 'E'

def is_active(uniqname):
	m = Member.objects.get(uniqname = uniqname)
	return m.status == 'A'