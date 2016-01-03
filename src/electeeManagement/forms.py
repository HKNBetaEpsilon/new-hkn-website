from django import forms

from .models import Requirements

class RequirementsForm(forms.Form):
	REQUIREMENTS = (
		('A_UG_SOCIAL', 'Number Undergrad Socials'),
		('B_G_SOCIAL', 'Number Grad Socials'),
		('C_UG_TOTAL_HOURS', 'Undergrad Total Service Hours'),
		('D_G_TOTAL_HOURS', 'Grad Total Service Hours'),
		('E_UG_DB_HOURS', 'Max Undergrad dB Service Hours'),
		('F_G_DB_HOURS', 'Max Grad dB Service Hours'),
		('G_UG_EXTERNAL_HOURS', 'Max Undergrad External Service Hours'),
		('H_G_EXTERNAL_HOURS', 'Max Grad External Service Hours'),
		('I_SINGLE_SERVICE_EVENT_HOURS', 'Max Hours for a Single Service Event'),
	)

	requirement = forms.ChoiceField(choices=REQUIREMENTS)
	num_required = forms.IntegerField()
