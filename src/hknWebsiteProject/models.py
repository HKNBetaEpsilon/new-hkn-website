from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.
from django.contrib.auth.models import User

class Requirements(models.Model):
	REQUIREMENTS = (
		('G_SOCIAL', 'Number Grad Socials'),
		('UG_SOCIAL', 'Number Undergrad Socials'),
		('G_TOTAL_HOURS', 'Grad Total Service Hours'),
		('UG_TOTAL_HOURS', 'Undergrad Total Service Hours'),
		('G_DB_HOURS', 'Max Grad dB Service Hours'),
		('UG_DB_HOURS', 'Max Undergrad dB Service Hours'),
		('G_EXTERNAL_HOURS', 'Max Grad External Service Hours'),
		('UG_EXTERNAL_HOURS', 'Max Undergrad External Service Hours'),
		('SINGLE_SERVICE_EVENT_HOURS', 'Max Single Service Event Hours'),
	)

	requirement = models.CharField(max_length=100, choices=REQUIREMENTS)
	num_required = models.IntegerField()

	def __unicode__(self):
		return self.requirement
