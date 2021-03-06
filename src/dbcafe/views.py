from hknWebsiteProject import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from .models import Item, Transaction, Drawer
from .forms import ItemForm, SalesForm
from hknWebsiteProject.utils import is_officer 

@login_required()
def items_list(request):
    context = {}
    if not (request.user.is_superuser or is_officer(request.user.username)):
        context = {
            'error': True,
            'error_msg': 'You do not have permission to access this page'
        }
    else:
        items = Item.objects.all()
        context = {
            'items': items
        }
    return render(request, "dbcafe/items_list.html", context)


@login_required()
def items_edit(request, item):
    context = {}
    if not (request.user.is_superuser or is_officer(request.user.username)):
        context = {
            'error': True,
            'error_msg': 'You do not have permission to access this page'
        }
    else:
        i = Item.objects.get(name=item)
        form = ItemForm(instance=i)
        context = {
            'form': form
        }
        if request.POST:
            form = ItemForm(request.POST, instance=i)
            if form.is_valid():
                form.save()
                return redirect('items_list')

    return render(request, "dbcafe/items_edit.html", context)


@login_required()
def items_add(request):
    context = {}
    if not (request.user.is_superuser or is_officer(request.user.username)):
        context = {
            'error': True,
            'error_msg': 'You do not have permission to access this page'
        }
    else:
        form = ItemForm(request.POST or None)
        context = {
            'form': form
        }

        if request.POST:
            form.save()
            return redirect('items_list')

    return render(request, "dbcafe/items_add.html", context)


@login_required()
def sales(request):
    context = {}
    if not (request.user.is_superuser or is_officer(request.user.username)):
        context = {
            'error': True,
            'error_msg': 'You do not have permission to access this page'
        }
    else:
        form = SalesForm(request.POST or None)
        drawer = Drawer.objects.all()[0]
        item_scanned = ''
        if form.is_valid():
            try:
                item_scanned = Item.objects.get(id_number=form.cleaned_data.get('item_id'))
                t = Transaction(item=item_scanned)
                item_scanned.quantity -= 1
                item_scanned.save()
                drawer.amount += item_scanned.price
                drawer.save()
                t.save()
            except Item.DoesNotExist:
                context['error'] = True

            form = SalesForm(None)

        transactions = Transaction.objects.order_by('-timestamp')[:10]
        context['form'] = form
        context['item_scanned'] = item_scanned
        context['transactions'] = transactions
    return render(request, "dbcafe/sales.html", context)


@login_required()
def stats(request):
    context = {}
    if not (request.user.is_superuser or is_officer(request.user.username)):
        context = {
            'error': True,
            'error_msg': 'You do not have permission to access this page'
        }
    else:
        drawer = Drawer.objects.all()[0]
        context = {
            'drawer': drawer
        }
    return render(request, "dbcafe/stats.html", context)


@login_required()
def reset(request):
    context = {}
    if not (request.user.is_superuser or is_officer(request.user.username)):
        context = {
            'error': True,
            'error_msg': 'You do not have permission to access this page'
        }
    else:
        drawer = Drawer.objects.all()[0]
        drawer.amount = 300
        drawer.save()
    return redirect('stats')


@login_required()
def undo(request):
    context = {}
    if not (request.user.is_superuser or is_officer(request.user.username)):
        context = {
            'error': True,
            'error_msg': 'You do not have permission to access this page'
        }
    else:
        transaction = Transaction.objects.all().order_by('-timestamp')[0]
        transaction.delete()
    return redirect('sales')
