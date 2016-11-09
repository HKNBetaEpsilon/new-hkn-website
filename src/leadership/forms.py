from django import forms
from django.forms.formsets import BaseFormSet

from .models import Leader

class LeaderModelForm(forms.ModelForm):
    class Meta:
        model = Leader
        exclude = ['member']


class DeleteLeaderForm(forms.Form):
    delete_leader = forms.ModelChoiceField(queryset=Leader.objects.all())
