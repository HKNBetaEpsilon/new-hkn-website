from __future__ import unicode_literals

from django.db import models

from users.models import Member
# Create your models here.

class Leader(models.Model):
	POSITION_TYPE = (
		('O', 'Officer'),
		('A', 'Advisor'),
		('C', 'Chair'),
	)

	position = models.CharField(max_length=100)
	member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
	position_type = models.CharField(max_length=1, choices=POSITION_TYPE, default='C')
	email = models.CharField(max_length=100, default='hkn-officers@umich.edu')

	def __unicode__(self):
		return self.position