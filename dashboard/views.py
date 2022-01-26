from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.models import User

from .forms import ProductForm

# Create your views here.


def error_404(request, exception):

    return render(request, 'dashboard/404.html')


@login_required
def index(request):

    context = {}

    return render(request, 'dashboard/index.html', context)


@login_required
def staff(request):
    workers = User.objects.all()

    context = {
        'workers': workers
    }

    return render(request, 'dashboard/staff.html', context)


@login_required
def staff_detail(request, pk):

    worker = User.objects.get(id=pk)

    context = {
        'worker': worker
    }

    return render(request, 'dashboard/staff_detail.html', context)

@login_required
def product(request):

    items = Product.objects.all()  # using ORM
    # items = Product.objects.raw('SELECT * FROM dashboard_product') #this allows us to write sql queries

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()

    context = {
        "items": items,
        'form': form
    }

    return render(request, 'dashboard/product.html', context)


@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('dashboard-product')

    context = {
        'item': item
    }

    return render(request, 'dashboard/product_delete.html', context)


@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-product")
    else:
        form = ProductForm(instance=item)

    context = {
        'item': item,
        'form': form
    }

    return render(request, 'dashboard/product_update.html', context)


@login_required
def order(request):

    context = {}

    return render(request, 'dashboard/order.html', context)
