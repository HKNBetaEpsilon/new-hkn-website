from django.shortcuts import render

from .models import Leader
from .forms import LeaderForm
# Create your views here.
from django.forms import modelformset_factory


def leadership(request):
	leaders = Leader.objects.all()
	context = {
		'leaders' : leaders
	}
	return render(request, "leadership.html", context)

def edit_leadership(request):
	context = {}
	if request.user.is_anonymous() or not request.user.is_superuser:
		context = {
			'error' : True,
			'error_msg' : 'You do not have permission to access this page'
		}
	else:
		leaders = Leader.objects.all().order_by('position')
		context = {
			'leaders' : leaders
		}
		
		# form  = LeaderForm(initial={'position': 'Hi there!'})

		# context['forms'] = forms
		# if request.POST:
		# 	print request.POST.dict()
		LeaderFormSet = modelformset_factory(Leader, fields=('member',), extra=0)
		aa = LeaderFormSet(queryset=Leader.objects.all().order_by('position'))
		context['aa'] = aa
	# 	context['leader_saved'] = False
	# 	l = Leader.objects.get(position = position)
	# 	form = LeaderForm(instance = l)	

		if request.POST:
			formset = LeaderFormSet(request.POST)
			formset.save()
			context['leader_saved'] = True
			return render(request, "leadership.html", context)
	# 		form = LeaderForm(request.POST, instance = l)
	# 		if form.is_valid():
	# 			form.save()
	# 			context['leader_saved'] = True		
	# 			return render(request, "leadership.html", context)

	# 	context['form'] = form

	return render(request, "edit_leadership.html", context)
