from __future__ import unicode_literals

from django.db import models

# Various hour requirements for electing that have to potential to change
# Model includes the name of the requirement and the number of hours
class Requirements(models.Model):
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

	requirement = models.CharField(max_length=100, choices=REQUIREMENTS, primary_key=True)
	num_required = models.IntegerField()

	def __unicode__(self):
		return self.requirement