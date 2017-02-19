from __future__ import unicode_literals

from users.models import Member

from django.db import models


# Model for keeping track of the progress of an electee on various electee requirements
class Electee(models.Model):
    # member for this electee
    member = models.OneToOneField(Member, on_delete=models.CASCADE, primary_key=True)

    # electee requirement progress
    num_socials_approved = models.IntegerField(default=0)
    num_socials_total = models.IntegerField(default=0)
    num_service_hours_approved = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    num_service_hours_total = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    num_service_hours_db = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    num_service_hours_hkn = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    num_service_hours_external = models.DecimalField(max_digits=6, decimal_places=1, default=0)
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
    # electee who submitted this social
    electee = models.ForeignKey(Electee, on_delete=models.CASCADE)

    social_name = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

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

    # electee who submitted these service hours
    electee = models.ForeignKey(Electee, on_delete=models.CASCADE)

    service_type = models.CharField(max_length=3, choices=SERVICE_TYPE)
    service_name = models.CharField(max_length=100)
    num_hours = models.DecimalField(max_digits=6, decimal_places=1)
    approved = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return self.electee.member.uniqname


# Various hour requirements for electing that have to potential to change
# Model includes the name of the requirement and the number of hours
class Requirements(models.Model):
    # alphabetized by the order in which they should be grouped/displayed
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
