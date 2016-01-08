from django import forms

from .models import Leader
from users.models import Member

class LeaderForm(forms.Form):
	new_leader = forms.ModelChoiceField(queryset=Member.objects.all())
	position = forms.CharField(max_length=100)
	widgets = {
			'new_leader': forms.Select(),
	}