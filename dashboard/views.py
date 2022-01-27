from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import ProductForm, OrderForm, ProductCategoryForm

# Create your views here.


def error_404(request, exception):

    return render(request, 'dashboard/404.html')


@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()

    workers_count = User.objects.all().count()
    orders_count = Order.objects.count()
    products_count = Product.objects.count()

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            product_name = instance.product.name
            messages.success(request, f"Order for {product_name} successful!")
            return redirect('dashboard-index')
    else:
        form = OrderForm()

    context = {
        'orders': orders,
        'form': form,
        'products': products,

        'workers_count': workers_count,
        'orders_count': orders_count,
        'products_count': products_count
    }

    return render(request, 'dashboard/index.html', context)


@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.count()
    products_count = Product.objects.count()


    context = {
        'workers': workers,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'products_count': products_count
    }

    return render(request, 'dashboard/staff.html', context)


@login_required
def staff_detail(request, pk):
    worker = User.objects.get(id=pk)
    workers_count = User.objects.all().count()
    orders_count = Order.objects.count()
    products_count = Product.objects.count()

    context = {
        'worker': worker,
        
        'workers_count': workers_count,
        'orders_count': orders_count,
        'products_count': products_count
    }

    return render(request, 'dashboard/staff_detail.html', context)


@login_required
def product(request):
    items = Product.objects.all()  # using ORM
    # items = Product.objects.raw('SELECT * FROM dashboard_product') #this allows us to write sql queries
    workers_count = User.objects.count()
    orders_count = Order.objects.count()
    products_count = items.count()

    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f"{product_name} has been added!")
            return redirect('dashboard-product')
    else:
        form = ProductForm()
        product_form = ProductCategoryForm()
        


    context = {
        "items": items,
        'form': form,
        'product_form': product_form,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'products_count': products_count
    }

    return render(request, 'dashboard/product.html', context)


@login_required
def create_product_category(request):

    if request.method == "POST":
        product_form = ProductCategoryForm(request.POST)

        if product_form.is_valid():
            product_form.save()
            product_name = product_form.cleaned_data.get('name')
            messages.success(request, f"{product_name} has been added!")
            return redirect('dashboard-product')
    else:
        product_form = ProductCategoryForm()

    context = {
        'product_form': product_form
    }

    return render(request, 'dashboard/product.html', context)


@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        product_name = item.name
        item.delete()
        messages.success(request, f"{product_name} has been deleted!")
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
            product_name = form.cleaned_data.get('name')
            messages.success(request, f"{product_name} updated successful!")
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
    orders = Order.objects.all()
    workers_count = User.objects.count()
    orders_count = orders.count()
    products_count = Product.objects.count()

    context = {
        'orders': orders,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'products_count': products_count
    }

    return render(request, 'dashboard/order.html', context)
