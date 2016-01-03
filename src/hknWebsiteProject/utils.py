from users.models import Member

def has_complete_profile(uniqname):
	m = Member.objects.get(uniqname = uniqname)
	if m.first_name and m.last_name and m.resume and m.profile_pic and m.major and m.edu_level and m.expected_grad_date:
		return True
	return False