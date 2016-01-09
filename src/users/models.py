from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
	return '{0}/{1}'.format(instance.uniqname, filename)

class Member(models.Model):
	STATUS = (
		('A', 'Active'),
		('E', 'Electee'),
		('O', 'Officer'),
	)

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

	uniqname = models.CharField(max_length=8, primary_key=True)
	first_name = models.CharField(max_length=100, null=True, blank=True)
	last_name = models.CharField(max_length=100, null=True, blank=True)
	status = models.CharField(max_length=1, choices=STATUS, default='E')
	major = models.CharField(max_length=2, choices=MAJOR, null=True, blank=True)
	edu_level = models.CharField(max_length=2, choices=EDU_LEVEL, null=True, blank=True)
	expected_grad_date = models.DateField(auto_now=False, auto_now_add=False, null=True,  blank=True)
	profile_pic =  models.ImageField(upload_to=user_directory_path, height_field=None, width_field=None, max_length=100, null=True,  blank=True)
	resume =  models.FileField(upload_to=user_directory_path, max_length=100, null=True,  blank=True)

	def __unicode__(self):
		return self.uniqname

	class Meta:
		ordering = ["uniqname"]

# Model for keeping track of the progress of an electee on various electee requirements
class Electee(models.Model):
	member = models.OneToOneField(Member, on_delete=models.CASCADE, primary_key=True)
	num_socials_approved = models.IntegerField(default=0)
	num_socials_total = models.IntegerField(default=0)
	num_service_hours_approved = models.IntegerField(default=0)
	num_service_hours_total = models.IntegerField(default=0)
	num_service_hours_db = models.IntegerField(default=0)
	num_service_hours_hkn = models.IntegerField(default=0)
	num_service_hours_external = models.IntegerField(default=0)
	electee_interview = models.BooleanField(default=False)
	electee_exam = models.BooleanField(default=False)
	dues = models.BooleanField(default=False)
	general_meetings_missed = models.IntegerField(default=0)

	def __unicode__(self):
		return self.member.uniqname

# Model for when an electee submits a social
# Includes the type of the name of the event, the number of hours, 
# 	and whether or not it has been approved
class Social(models.Model):
	electee = models.ForeignKey(Electee, on_delete=models.CASCADE)
	social_name = models.CharField(max_length=100)
	approved = models.BooleanField(default=False)

	def __unicode__(self):
		return self.electee.member.uniqname

# Model for when an electee submits a service event
# Includes the type of service event, the name of the event, 
# 	the number of hours, and whether or not it has been approved
class Service_Hours(models.Model):
	SERVICE_TYPE = (
		('dB', 'dB Cafe'),
		('HKN', 'HKN'),
		('Ex', 'External'),
	)

	electee = models.ForeignKey(Electee, on_delete=models.CASCADE)
	service_type = models.CharField(max_length=3, choices=SERVICE_TYPE)
	service_name = models.CharField(max_length=100)
	num_hours = models.IntegerField()
	approved = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.electee.member.uniqname
