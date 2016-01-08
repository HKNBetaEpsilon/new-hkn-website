from django.shortcuts import render, redirect

from .models import Leader
from .forms import LeaderForm, LeaderModelForm, DeleteLeaderForm
# Create your views here.
from django.forms import modelformset_factory

def leadership(request, leader_saved=0):
	context = {}
	leaders = Leader.objects.all().filter(member__isnull=False).order_by('-display_order')
	context['leaders'] = leaders
	context['leader_saved'] = leader_saved
	return render(request, "leadership.html", context)

def edit_leadership(request, position_added=0):
	context = {}
	if request.user.is_anonymous() or not request.user.is_superuser:
		context = {
			'error' : True,
			'error_msg' : 'You do not have permission to access this page'
		}
	else:
		leaders = Leader.objects.all().order_by('-display_order')
		context = {
			'leaders' : leaders,
			'position_added' : position_added
		}

		LeaderFormSet = modelformset_factory(Leader, fields=('member',), extra=0)
		aa = LeaderFormSet(queryset=Leader.objects.all().order_by('-display_order'))
		context['aa'] = aa

		if request.POST:
			formset = LeaderFormSet(request.POST)
			formset.save()
			return redirect('leadership', leader_saved=1)

	return render(request, "edit_leadership.html", context)

def add_leadership(request):
	context = {}
	if request.user.is_anonymous() or not request.user.is_superuser:
		context = {
			'error' : True,
			'error_msg' : 'You do not have permission to access this page'
		}
	else:
		form = LeaderModelForm()
		context['form'] = form

		if request.POST:
			form = LeaderModelForm(request.POST)
			form.save()
			return redirect('edit_leadership', position_added=1)

	return render(request, "add_leadership.html", context)

def delete_leader(request):
	context = {}
	form = DeleteLeaderForm()
	context['form'] = form

	if request.POST:
		form = DeleteLeaderForm(request.POST)
		if form.is_valid():
			position = form.cleaned_data.get('delete_leader').position
			leader = Leader.objects.get(position__exact=position)
			leader.delete()
			return redirect('edit_leadership', position_added=1)
	return render(request, "delete_leader.html", context)
