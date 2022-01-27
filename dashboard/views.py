from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import OrderForm, ProductCategoryForm, ProductForm
from .models import Order, Product, ProductCategory

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
            messages.success(request, f"Order for {product_name} placed successful!")
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
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(
                request, f"Product with name {product_name} updated successful!")
            return redirect("dashboard-product")
    else:
        form = ProductForm(instance=item)

    context = {
        'item': item,
        'form': form
    }

    return render(request, 'dashboard/product_update.html', context)


@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        product_name = item.name
        item.delete()
        messages.success(
            request, f"Product with name {product_name} has been deleted!")
        return redirect('dashboard-product')

    context = {
        'item': item
    }

    return render(request, 'dashboard/product_delete.html', context)


@login_required
def order(request):
    orders = Order.objects.all()
    workers_count = User.objects.count()
    orders_count = Order.objects.count()
    products_count = Product.objects.count()

    context = {
        'orders': orders,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'products_count': products_count
    }

    return render(request, 'dashboard/order.html', context)


@login_required
def order_update(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            order_name = order.product.name
            messages.success(
                request, f"Order with name {order_name} updated successful!")
            return redirect("dashboard-index")
    else:
        form = OrderForm(instance=order)

    context = {
        'order': order,
        'form': form
    }

    return render(request, 'dashboard/order_update.html', context)


@login_required
def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order_name = order.product.name
        order.delete()
        messages.success(
            request, f"Order with name {order_name} has been deleted!")
        return redirect('dashboard-index')

    context = {
        'order': order
    }

    return render(request, 'dashboard/order_delete.html', context)


@login_required
def category(request):
    categories = ProductCategory.objects.all()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.count()
    products_count = Product.objects.count()

    context = {
        'categories': categories,

        'workers_count': workers_count,
        'orders_count': orders_count,
        'products_count': products_count
    }

    return render(request, 'dashboard/categories.html', context)


@login_required
def create_product_category(request):

    if request.method == "POST":
        product_form = ProductCategoryForm(request.POST)

        if product_form.is_valid():
            product_form.save()
            product_name = product_form.cleaned_data.get('name')
            messages.success(
                request, f"Category {product_name} has been added!")
            return redirect('dashboard-product')
    else:
        product_form = ProductCategoryForm()

    context = {
        'product_form': product_form
    }

    return render(request, 'dashboard/product.html', context)


@login_required
def category_update(request, pk):
    category = ProductCategory.objects.get(id=pk)
    if request.method == "POST":
        form = ProductCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            category_name = form.cleaned_data.get('name')
            messages.success(
                request, f"Category with name {category_name} updated successful!")
            return redirect("dashboard-product-categories")
    else:
        form = ProductCategoryForm(instance=category)

    context = {
        'category': category,
        'form': form
    }

    return render(request, 'dashboard/category_update.html', context)


@login_required
def category_delete(request, pk):
    category = ProductCategory.objects.get(id=pk)
    if request.method == "POST":
        category_name = category.name
        category.delete()
        messages.success(
            request, f"Category with name {category_name} has been deleted!")
        return redirect('dashboard-product-categories')

    context = {
        'category': category
    }

    return render(request, 'dashboard/category_delete.html', context)
