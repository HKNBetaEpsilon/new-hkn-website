from django.shortcuts import render, redirect

# Create your views here.

from users.forms import Member
from .forms import SocialForm, ServiceHoursForm
from .models import Electee, Social, Service_Hours, Requirements

from django.forms import modelformset_factory


def update_approved_hours():
    all_electees = Electee.objects.all()
    for e in all_electees:
        e.num_socials_approved = Social.objects.filter(electee=e).filter(approved='1').count()

        e.num_service_hours_approved = 0
        service_hours = Service_Hours.objects.filter(electee=e).filter(approved='1')
        for event in service_hours:
            e.num_service_hours_approved += event.num_hours
        e.save()


# display all of the electee objects in a list, should only be viewable by officers
def all_electees(request):
    # get all of the electee objects to display
    electee_list = Electee.objects.filter(member__status='E')
    requirements = dict(
        (requirements.requirement, requirements) for requirements in Requirements.objects.all())

    context = {
        'electee_list': electee_list,
        'requirements': requirements
    }

    return render(request, "all_electees.html", context)


def submit_social(request):
    m = Member.objects.get(uniqname=request.user.username)
    # error if the request user is anonymous or not an electee
    if request.user.is_anonymous() or not m.is_electee():
        context = {
            'error': True,
            'error_msg': 'You must be an electee to submit socials'
        }
    else:
        context = {
            'error': False,
            'social_submitted': False
        }

        form = SocialForm(request.POST or None)
        if request.POST:
            if form.is_valid():
                social = form.save(commit=False)
                # set the electee field on the social model
                social.electee = Electee.objects.get(member_id=request.user.username)
                social.save()

                electee = Electee.objects.get(member_id=request.user.username)
                electee.num_socials_total = electee.num_socials_total + 1
                electee.save()

                # display a new blank form
                form = SocialForm(None)

                # show green bar at top of page saying that a social has been submitted
                context['social_submitted'] = True

        context['form'] = form

    return render(request, "submit_social.html", context)


def submit_service_hours(request):
    m = Member.objects.get(uniqname=request.user.username)
    # error if the request user is anonymous or not an electee
    if request.user.is_anonymous() or not m.is_electee():
        context = {
            'error': True,
            'error_msg': 'You must be an electee to submit service hours'
        }
    else:
        context = {
            'error': False,
            'service_hours_submitted': False
        }

        form = ServiceHoursForm(request.POST or None)
        if request.POST:
            if form.is_valid():
                service_hours = form.save(commit=False)
                # set the electee field on the service_hours model
                service_hours.electee = Electee.objects.get(member_id=request.user.username)
                service_hours.save()

                electee = Electee.objects.get(member_id=request.user.username)
                electee.num_service_hours_total = electee.num_service_hours_total + service_hours.num_hours
                if service_hours.service_type == 'dB':
                    electee.num_service_hours_db = electee.num_service_hours_db + service_hours.num_hours
                elif service_hours.service_type == 'HKN':
                    electee.num_service_hours_hkn = electee.num_service_hours_hkn + service_hours.num_hours
                else:
                    electee.num_service_hours_external = electee.num_service_hours_external + service_hours.num_hours
                electee.save()

                # display a new blank form
                form = ServiceHoursForm(None)

                # show green bar at top of page saying that a service hours have been submitted
                context['service_hours_submitted'] = True

        context['form'] = form

    return render(request, "submit_service_hours.html", context)


# shows a list of all unapporved socials and service hours
def electee_submission_approval(request, approved=0):
    # get all unapproved socials and service hours
    social_list = Social.objects.filter(approved='0')
    service_hour_list = Service_Hours.objects.filter(approved='0')

    SocialFormSet = modelformset_factory(Social, fields=('approved',), extra=0)
    social_formset = SocialFormSet(
        queryset=Social.objects.filter(approved='0').order_by('timestamp'))

    ServiceFormSet = modelformset_factory(Service_Hours, fields=('approved',), extra=0)
    service_formset = ServiceFormSet(
        queryset=Service_Hours.objects.filter(approved='0').order_by('timestamp'))

    context = {
        'social_list': social_list,
        'service_hour_list': service_hour_list,
        'social_formset': social_formset,
        'service_formset': service_formset,
        'approved': approved
    }

    if request.POST:
        formset = SocialFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            update_approved_hours()
        formset = ServiceFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            update_approved_hours()
        return redirect('electee_submission_approval', approved=1)

    return render(request, "electee_submission_approval.html", context)


def edit_electee_requirements(request):
    RequirementsFormset = modelformset_factory(Requirements, fields=('num_required',), extra=0)
    req_formset = RequirementsFormset(queryset=Requirements.objects.all())

    context = {
        'req_formset': req_formset,
        'requirement_changed': False
    }

    if request.POST:
        formset = RequirementsFormset(request.POST)
        formset.save()
        context['requirement_changed'] = True

    return render(request, "edit_electee_requirements.html", context)


def initilize_electee_requirements(request):
    context = {
        'submitted': False
    }

    if request.POST:
        a = Requirements(requirement='A_UG_SOCIAL', num_required=0)
        a.save()
        b = Requirements(requirement='B_G_SOCIAL', num_required=0)
        b.save()
        c = Requirements(requirement='C_UG_TOTAL_HOURS', num_required=0)
        c.save()
        d = Requirements(requirement='D_G_TOTAL_HOURS', num_required=0)
        d.save()
        e = Requirements(requirement='E_UG_DB_HOURS', num_required=0)
        e.save()
        f = Requirements(requirement='F_G_DB_HOURS', num_required=0)
        f.save()
        g = Requirements(requirement='G_UG_EXTERNAL_HOURS', num_required=0)
        g.save()
        h = Requirements(requirement='H_G_EXTERNAL_HOURS', num_required=0)
        h.save()
        i = Requirements(requirement='I_SINGLE_SERVICE_EVENT_HOURS', num_required=0)
        i.save()

        context['submitted'] = True

    return render(request, "initilize_electee_requirements.html", context)


def electee_turn_ins(request):
    TurnInsFormset = modelformset_factory(Electee,
                                          fields=('electee_interview', 'dues', 'electee_exam'),
                                          extra=0)
    turnins_formset = TurnInsFormset(queryset=Electee.objects.all())
    context = {
        'turnins_formset': turnins_formset
    }

    if request.POST:
        formset = TurnInsFormset(request.POST)
        formset.save()
        context['turnins_saved'] = True

    return render(request, "electee_turn_ins.html", context)
