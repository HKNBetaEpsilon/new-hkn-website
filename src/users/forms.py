from django import forms

from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ['uniqname', 'status']
        widgets = {
            'graduation_date': forms.TextInput(attrs={'class': 'datepicker'}),
        }

    # Scketchy way of making all fields required in form
    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True
        self.fields['resume'].required = False

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume == None or resume == False:
            return resume
        resume_parts = resume.name.split('.')
        extension = resume_parts[-1]
        if extension != 'pdf' and extension != 'PDF':
            raise forms.ValidationError("Resumes must be a PDF document")
        return resume


# Form to submit a comma separated list of new member to create member objects for
class NewMemberForm(forms.Form):
    new_members = forms.CharField()
    status = (('E', 'Electee'),
              ('A', 'Active'))
    type = forms.ChoiceField(choices=status)

    def clean_new_members(self):
        new_members = self.cleaned_data.get('new_members')

        uniqnames = new_members.split(',')
        for name in uniqnames:
            if len(name) < 3 or len(name) > 8:
                raise forms.ValidationError("A Uniqname is either too long or too short:" + name)
            if not str(name).isalpha():
                raise forms.ValidationError(
                    "A Uniqname has a non alphabetical character in it" + name)
        return new_members
