from django import forms

from .models import Leader


# class LeaderForm(forms.Form):
# 	new_leader = forms.ModelChoiceField(queryset=Member.objects.all())
# 	position = forms.CharField(max_length=100)
# 	widgets = {
# 			'new_leader': forms.Select(),
# 	}

class LeaderModelForm(forms.ModelForm):
    class Meta:
        model = Leader
        exclude = ['member']


class DeleteLeaderForm(forms.Form):
    delete_leader = forms.ModelChoiceField(queryset=Leader.objects.all())
