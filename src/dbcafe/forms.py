from django import forms

from .models import Item

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		exclude = ['',]

class SalesForm(forms.Form):
	item_id = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'autofocus'}))
