from django.shortcuts import render, redirect

# Create your views here.
from .models import Item, Transaction, Drawer
from .forms  import ItemForm, SalesForm

def items_list(request):
	items = Item.objects.all()
	context = {
		'items' : items
	}
	return render(request, "items_list.html", context)


def items_edit(request, item):
	i = Item.objects.get(name = item)
	form = ItemForm(instance = i)
	context = {
		'form' : form
	}
	if request.POST:
			form = ItemForm(request.POST, instance = i)
			if form.is_valid():
				form.save()
				return redirect('items_list')

	return render(request, "items_edit.html", context)

def items_add(request):
	form = ItemForm(request.POST or None)
	context = {
		'form' : form
	}

	if request.POST:
		form.save()
		return redirect('items_list')

	return render(request, "items_add.html", context)

def sales(request):
	context = {}
	form = SalesForm(request.POST or None)
	drawer = Drawer.objects.all()[0]
	item_scanned = ''
	if form.is_valid():
		try:
			item_scanned = Item.objects.get(id_number = form.cleaned_data.get('item_id'))
			t = Transaction(item=item_scanned)
			item_scanned.quantity -= 1
			item_scanned.save()
			drawer.amount += item_scanned.price
			drawer.save()
			t.save()
		except Item.DoesNotExist:
			context['error'] = True

		form = SalesForm(None)

	transactions = Transaction.objects.all().order_by('-timestamp')
	context['form'] = form
	context['item_scanned'] = item_scanned
	context['transactions'] = transactions
	return render(request, "sales.html", context)

def stats(request):
	drawer = Drawer.objects.all()[0]
	context = {
		'drawer' : drawer
	}
	return render(request, "stats.html", context)

def reset(request):
	drawer = Drawer.objects.all()[0]
	drawer.amount = 300
	drawer.save()
	return redirect('stats')

def undo(request):
	transaction = Transaction.objects.all().order_by('-timestamp')[0]
	transaction.delete()
	return redirect('sales')