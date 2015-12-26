from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
	return '{0}/{1}'.format(instance.uniqname, filename)

class Member(models.Model):
	MAJOR = (
		('CS', 'Computer Science'),
		('CE', 'Computer Engineering'),
		('EE', 'Electrical Engineering'),
	)

	EDU_LEVEL = (
		('UG', 'Undergraduate'),
		('GR', 'Graduate'),
		('AL', 'Alumni'),
	)

	uniqname = models.CharField(max_length=8)
	first_name = models.CharField(max_length=100, null=True, blank=True)
	last_name = models.CharField(max_length=100, null=True, blank=True)
	major = models.CharField(max_length=2, choices=MAJOR, null=True, blank=True)
	edu_level = models.CharField(max_length=2, choices=EDU_LEVEL, null=True, blank=True)
	expected_grad_date = models.DateField(auto_now=False, auto_now_add=False, null=True,  blank=True)
	profile_pic =  models.ImageField(upload_to=user_directory_path, height_field=None, width_field=None, max_length=100, null=True,  blank=True)
	resume =  models.FileField(upload_to=user_directory_path, max_length=100, null=True,  blank=True)

	def __unicode__(self):
		return self.uniqname
