from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['publicationDate', ]
    def __init__(self, *args, **kwargs):
    	self.helper = FormHelper()
    	self.helper.form_id = 'Blog Form'
    	self.helper.form_class = 'blog-form'
    	self.helper.form_method = 'post'
    	self.helper.form_action = ''
    	self.helper.add_input(Submit('submit', 'Submit'))
    	super(BlogForm, self).__init__(*args, **kwargs)