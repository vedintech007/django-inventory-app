from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def error_404(request, exception):

    return render(request, 'dashboard/404.html')


@login_required
def index(request):

    context = {}

    return render(request, 'dashboard/index.html', context)


@login_required
def staff(request):

    context = {}

    return render(request, 'dashboard/staff.html', context)


@login_required
def product(request):

    context = {}

    return render(request, 'dashboard/product.html', context)


@login_required
def order(request):

    context = {}

    return render(request, 'dashboard/order.html', context)
