from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=120, primary_key=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	quantity = models.IntegerField()
	id_number = models.CharField(max_length=120, null=True)

	def __unicode__(self):
		return self.name

class Transaction(models.Model):
	item = models.ForeignKey(Item, on_delete=models.PROTECT)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.item.name

class Drawer(models.Model):
	amount = models.DecimalField(max_digits=999, decimal_places=2)
